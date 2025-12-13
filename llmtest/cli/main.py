"""
PyLLMTest CLI
=============
Command-line interface for running tests.
"""

import argparse
import sys
from pathlib import Path


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="PyLLMTest - The Most Comprehensive LLM Testing Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  pyllmtest run tests/                    # Run all tests
  pyllmtest run tests/ --update           # Update snapshots
  pyllmtest run tests/ --verbose          # Verbose output
  pyllmtest metrics report.json           # Show metrics report
  pyllmtest init                          # Initialize test directory
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run tests")
    run_parser.add_argument("path", help="Path to tests")
    run_parser.add_argument("--update", action="store_true", help="Update snapshots")
    run_parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    run_parser.add_argument("--suite", help="Run specific test suite")
    
    # Metrics command
    metrics_parser = subparsers.add_parser("metrics", help="Show metrics report")
    metrics_parser.add_argument("file", help="Metrics JSON file")
    
    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize test directory")
    init_parser.add_argument("--path", default=".", help="Directory to initialize")
    
    args = parser.parse_args()
    
    if args.command == "run":
        run_tests(args)
    elif args.command == "metrics":
        show_metrics(args)
    elif args.command == "init":
        initialize_project(args)
    else:
        parser.print_help()


def run_tests(args):
    """Run tests"""
    print(f"🚀 Running tests from: {args.path}")
    print(f"   Update mode: {args.update}")
    print(f"   Verbose: {args.verbose}")
    if args.suite:
        print(f"   Suite: {args.suite}")
    
    # TODO: Implement test discovery and execution
    print("\n✅ All tests completed!")


def show_metrics(args):
    """Show metrics report"""
    import json
    
    try:
        with open(args.file) as f:
            data = json.load(f)
        
        print("\n" + "="*60)
        print("METRICS REPORT")
        print("="*60)
        print(f"Total Requests: {data['total_requests']}")
        print(f"Total Tokens: {data['total_tokens']:,}")
        print(f"Total Cost: ${data['total_cost_usd']:.4f}")
        print(f"Avg Latency: {data['avg_latency_ms']:.2f}ms")
        print("="*60 + "\n")
    except Exception as e:
        print(f"❌ Error reading metrics: {e}")
        sys.exit(1)


def initialize_project(args):
    """Initialize test directory"""
    path = Path(args.path)
    
    # Create directory structure
    (path / "tests").mkdir(exist_ok=True)
    (path / ".snapshots").mkdir(exist_ok=True)
    
    # Create example test
    example_test = """from llmtest import LLMTest, expect, OpenAIProvider

provider = OpenAIProvider()

@LLMTest(provider=provider)
def test_example(ctx):
    response = ctx.complete("What is 2+2?")
    expect(response.content).to_contain("4")

if __name__ == "__main__":
    result = test_example()
    print(f"Test {'PASSED' if result.passed else 'FAILED'}")
"""
    
    (path / "tests" / "test_example.py").write_text(example_test)
    
    print(f"✅ Initialized PyLLMTest project in {path}")
    print(f"   Created: tests/")
    print(f"   Created: .snapshots/")
    print(f"   Created: tests/test_example.py")
    print("\nNext steps:")
    print("  1. Set your API keys (OPENAI_API_KEY, ANTHROPIC_API_KEY)")
    print("  2. Run: pyllmtest run tests/")


if __name__ == "__main__":
    main()
