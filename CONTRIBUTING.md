# Contribution Documentation for Issue #1030: Fixing Insert Operation in Supabase Python Client

## Project Description
The Supabase Python Client (supabase-py) is an open-source library that allows Python developers to interact with Supabase services, including database operations, authentication, file storage, and real-time data streaming. With over 1.9k stars and 223 forks, the project is widely used and maintained by an active community. It provides an easy-to-use interface for integrating back-end services into modern applications.

## Contribution Overview
**Issue Addressed:** Issue #1030 – "Inserting a row to a table does not work."  
**Problem:** When inserting a row into a table (specifically, the `test3` table), the API call initially returned an empty data array due to restrictive row-level security (RLS) policies.  
**Solution:** I resolved the issue by adding a test script (`insert_test.py`) that reproduces the problem and verifies that, if the insert operation returns empty data, a follow-up select query retrieves the inserted row.  
**Technologies Used:** Python, REST API, Supabase, PostgREST

## GitHub File Walkthrough
- **Files Modified:**
  - **`insert_test.py`**:  
    This new test script was added to reproduce the bug and verify the fix. The script attempts to insert a row into the `test3` table. If the insert returns an empty data array, it automatically issues a select query to retrieve the inserted row.
- **Key Changes:**
  - The test script demonstrates the issue by printing the initial insert response.
  - It includes logic to perform a follow-up select query if the insert response is empty, ensuring that the inserted row is eventually retrieved.
  - No other files were changed for this contribution.

## Contribution Walkthrough
1. **Setup:**
   - Forked the upstream repository and created a new branch called `Open-source-Contribution`.
   - Configured a local Supabase instance with a test table named `test3` and set up the necessary RLS policies for both insert and select operations.
2. **Reproducing the Bug:**
   - Ran `insert_test.py` to confirm that an insert operation initially returned an empty data array due to the RLS policies.
3. **Implementing the Fix:**
   - Added the `insert_test.py` script to include logic that checks if the insert response is empty.
   - If empty, the script automatically issues a select query to retrieve the inserted row.
   - Verified the fix by re-running `insert_test.py` and confirming that the inserted data was successfully retrieved.
4. **Testing and Verification:**
   - The output from the test script confirmed that the fix effectively resolves Issue #1030.

## GitHub Links
- **GitHub Branch URL:** [https://github.com/NealShankarGit/supabase/tree/Open-source-Contribution](https://github.com/NealShankarGit/supabase/tree/Open-source-Contribution)
- **Pull Request:** [https://github.com/NealShankarGit/supabase/pull/new/Open-source-Contribution](https://github.com/NealShankarGit/supabase/pull/new/Open-source-Contribution)

## General Contribution Guidelines

We highly appreciate feedback and contributions from the community! Please review and follow the guidelines below.

### Code of Conduct
In the interest of fostering an open and welcoming environment, please review and follow our [code of conduct](./CODE_OF_CONDUCT.md).

### Code and Copy Reviews
All submissions, including those by project members, require review. We use GitHub pull requests for this purpose. After filing a pull request, please tag any two of the [current maintainers](./MAINTAINERS.md) to request a review.

### Reporting Issues / Filing Feature Requests
Before opening a new issue or feature request, please check existing issues and discussions to ensure your topic hasn’t already been addressed. Report all issues and file all feature requests through [GitHub Issues](./issues).

### Creating a Pull Request
When making pull requests to the repository, please adhere to the following guidelines:
- File a GitHub Issue before creating a pull request so that maintainers and the community can discuss the problem and potential solutions.
- In your PR's description, link to any related issues or pull requests to give reviewers the full context of your change (e.g., use `#1030` to reference this issue).
- Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format for commit messages (e.g., `docs: updated contribution documentation`).




