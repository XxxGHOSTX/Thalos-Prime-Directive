#!/usr/bin/env python3
"""
© 2026 Tony Ray Macier III. All rights reserved.

Thalos Prime is an original proprietary software system, including but not limited to
its source code, system architecture, internal logic descriptions, documentation,
interfaces, diagrams, and design materials.

Unauthorized reproduction, modification, distribution, public display, or use of
this software or its associated materials is strictly prohibited without the
express written permission of the copyright holder.

Thalos Prime™ is a proprietary system.
"""

"""
Thalos Prime v1.0 - Test Runner Script

Runs all unit and integration tests and provides a summary.
"""

import os
import sys
import subprocess
import time

# Colors for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'


def run_test_file(filepath):
    """Run a single test file and return success status"""
    try:
        result = subprocess.run(
            [sys.executable, filepath],
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Test timed out"
    except Exception as e:
        return False, "", str(e)


def count_tests_in_output(output):
    """Count the number of tests passed from output"""
    count = output.count('✓')
    return count


def main():
    """Main test runner"""
    print(f"{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}   Thalos Prime v1.0 - Test Runner{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}")
    print()
    
    # Get project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(project_root, 'tests')
    unit_dir = os.path.join(tests_dir, 'unit')
    integration_dir = os.path.join(tests_dir, 'integration')
    
    start_time = time.time()
    results = {
        'passed': [],
        'failed': []
    }
    total_tests = 0
    
    # Run unit tests
    print(f"{BOLD}Running Unit Tests...{RESET}")
    print("-" * 40)
    
    unit_test_files = sorted([
        f for f in os.listdir(unit_dir)
        if f.startswith('test_') and f.endswith('.py')
    ])
    
    for test_file in unit_test_files:
        filepath = os.path.join(unit_dir, test_file)
        print(f"  Running {test_file}...", end=" ")
        success, stdout, stderr = run_test_file(filepath)
        
        if success:
            test_count = count_tests_in_output(stdout)
            total_tests += test_count
            results['passed'].append(test_file)
            print(f"{GREEN}PASSED{RESET} ({test_count} tests)")
        else:
            results['failed'].append(test_file)
            print(f"{RED}FAILED{RESET}")
            if stderr:
                print(f"    {RED}Error: {stderr[:100]}{RESET}")
    
    print()
    
    # Run integration tests
    print(f"{BOLD}Running Integration Tests...{RESET}")
    print("-" * 40)
    
    integration_test_files = sorted([
        f for f in os.listdir(integration_dir)
        if f.startswith('test_') and f.endswith('.py')
    ])
    
    for test_file in integration_test_files:
        filepath = os.path.join(integration_dir, test_file)
        print(f"  Running {test_file}...", end=" ")
        success, stdout, stderr = run_test_file(filepath)
        
        if success:
            test_count = count_tests_in_output(stdout)
            total_tests += test_count
            results['passed'].append(test_file)
            print(f"{GREEN}PASSED{RESET} ({test_count} tests)")
        else:
            results['failed'].append(test_file)
            print(f"{RED}FAILED{RESET}")
            if stderr:
                print(f"    {RED}Error: {stderr[:100]}{RESET}")
    
    # Calculate elapsed time
    elapsed_time = time.time() - start_time
    
    # Print summary
    print()
    print(f"{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}   Test Summary{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}")
    print()
    print(f"  Total Tests Run:    {total_tests}")
    print(f"  Test Files Passed:  {GREEN}{len(results['passed'])}{RESET}")
    print(f"  Test Files Failed:  {RED}{len(results['failed'])}{RESET}")
    print(f"  Elapsed Time:       {elapsed_time:.2f}s")
    print()
    
    if results['failed']:
        print(f"{RED}Failed Tests:{RESET}")
        for test in results['failed']:
            print(f"  - {test}")
        print()
        print(f"{RED}{BOLD}TESTS FAILED{RESET}")
        return 1
    else:
        print(f"{GREEN}{BOLD}ALL TESTS PASSED! ✓{RESET}")
        return 0


if __name__ == "__main__":
    sys.exit(main())
