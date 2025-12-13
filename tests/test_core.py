"""
Basic Tests for PyLLMTest
==========================
Verify core functionality works.
"""

import sys
sys.path.insert(0, '/home/claude/pyllmtest')

def test_imports():
    """Test that all imports work"""
    print("Testing imports...")
    
    try:
        from llmtest import (
            LLMTest,
            expect,
            SnapshotManager,
            MetricsTracker,
            RAGTester,
            PromptOptimizer,
        )
        print("✓ Core imports successful")
        
        from llmtest.providers.base import BaseLLMProvider, LLMResponse
        print("✓ Provider imports successful")
        
        from llmtest.core.assertions import Expectation
        print("✓ Assertion imports successful")
        
        from llmtest.core.snapshot import Snapshot
        print("✓ Snapshot imports successful")
        
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False


def test_assertions():
    """Test assertion system"""
    print("\nTesting assertions...")
    
    try:
        from llmtest import expect
        
        # String assertions
        text = "Hello World! This is a test."
        expect(text).to_contain("Hello")
        expect(text).to_start_with("Hello")
        expect(text).not_to_contain("Goodbye")
        expect(text).to_be_shorter_than(100, unit="chars")
        expect(text).to_be_longer_than(10, unit="chars")
        
        print("✓ String assertions work")
        
        # Length assertions
        expect("short").to_be_between(1, 10, unit="chars")
        expect("one two three").to_be_between(2, 5, unit="words")
        
        print("✓ Length assertions work")
        
        # Boolean assertions
        expect(True).to_be_true()
        expect(False).to_be_false()
        expect(5).to_equal(5)
        
        print("✓ Boolean assertions work")
        
        return True
    except Exception as e:
        print(f"✗ Assertion test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_snapshot_manager():
    """Test snapshot manager"""
    print("\nTesting snapshot manager...")
    
    try:
        from llmtest import SnapshotManager
        import tempfile
        import shutil
        
        # Create temporary directory
        temp_dir = tempfile.mkdtemp()
        
        try:
            mgr = SnapshotManager(snapshot_dir=temp_dir, update_mode=True)
            
            # Save a snapshot
            snapshot = mgr.save_snapshot(
                name="test_snap",
                content="Test content",
                metadata={"version": 1}
            )
            print(f"✓ Saved snapshot: {snapshot.name}")
            
            # Load it back
            loaded = mgr.load_snapshot("test_snap")
            assert loaded.content == "Test content"
            print("✓ Loaded snapshot successfully")
            
            # Compare
            result = mgr.compare("test_snap", "Test content")
            assert result["matched"]
            print("✓ Snapshot comparison works")
            
            # List snapshots
            snapshots = mgr.list_snapshots()
            assert "test_snap" in snapshots
            print("✓ Snapshot listing works")
            
        finally:
            # Cleanup
            shutil.rmtree(temp_dir)
        
        return True
    except Exception as e:
        print(f"✗ Snapshot test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_metrics_tracker():
    """Test metrics tracker"""
    print("\nTesting metrics tracker...")
    
    try:
        from llmtest import MetricsTracker
        from llmtest.providers.base import LLMResponse
        from datetime import datetime
        
        tracker = MetricsTracker()
        
        # Create fake responses
        for i in range(3):
            response = LLMResponse(
                content=f"Response {i}",
                model="test-model",
                provider="TestProvider",
                tokens_used=100 + i * 10,
                prompt_tokens=50 + i * 5,
                completion_tokens=50 + i * 5,
                latency_ms=100.0 + i * 10,
                cost_usd=0.001 + i * 0.0001,
                timestamp=datetime.now(),
                metadata={},
                raw_response=None
            )
            tracker.track_request(response)
        
        print("✓ Tracked 3 requests")
        
        # Get summary
        summary = tracker.get_summary()
        assert summary.total_requests == 3
        assert summary.total_tokens == 330  # 100+110+120
        print("✓ Summary calculation works")
        
        # Get breakdowns
        breakdown = tracker.get_cost_breakdown()
        assert breakdown["total"] > 0
        print("✓ Cost breakdown works")
        
        return True
    except Exception as e:
        print(f"✗ Metrics test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_providers():
    """Test provider base classes"""
    print("\nTesting provider base classes...")
    
    try:
        from llmtest.providers.base import BaseLLMProvider, LLMResponse
        
        # Can't instantiate abstract class, but can check it exists
        assert BaseLLMProvider is not None
        print("✓ BaseLLMProvider exists")
        
        # Check LLMResponse
        from datetime import datetime
        response = LLMResponse(
            content="test",
            model="test-model",
            provider="TestProvider",
            tokens_used=100,
            prompt_tokens=50,
            completion_tokens=50,
            latency_ms=100.0,
            cost_usd=0.001,
            timestamp=datetime.now(),
            metadata={},
            raw_response=None
        )
        assert response.content == "test"
        print("✓ LLMResponse works")
        
        return True
    except Exception as e:
        print(f"✗ Provider test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("PyLLMTest - Core Functionality Tests")
    print("="*60)
    
    tests = [
        ("Imports", test_imports),
        ("Assertions", test_assertions),
        ("Snapshot Manager", test_snapshot_manager),
        ("Metrics Tracker", test_metrics_tracker),
        ("Providers", test_providers),
    ]
    
    passed = 0
    failed = 0
    
    for name, test_fn in tests:
        try:
            if test_fn():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"\n✗ {name} failed with exception: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*60)
    
    if failed == 0:
        print("\n✨ All tests passed! PyLLMTest is working correctly. ✨\n")
    else:
        print(f"\n⚠️  {failed} test(s) failed. Please check the errors above.\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
