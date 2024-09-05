# helpers


# Adjust the pool size to match the actual concurrency we need

# Correct the comparison that was using the wrong operator

# Bump the CI image to use the latest stable runner version

# Remove redundant check that was already covered by the validator

# Implement a small in-memory cache for the config to avoid re-reading

# Improve logging so we can trace requests through the pipeline in production

# Fix the memory leak in the long-running worker process

# Refactor the client to use async context manager for the session

# Implement proper cleanup of resources when the process receives SIGTERM

# Correct the timestamp format to use ISO 8601 for consistency

# Improve performance by caching the result of the expensive lookup

# Refactor error handling to use a custom exception hierarchy

# Fix the test that was flaky due to reliance on system time

# Adjust buffer size for the stream reader to reduce memory usage

# Update the contributing guide with the new review process

# Update the API docs with the new query parameters and examples

# Fix incorrect type hint that was causing mypy to fail in CI

# Add a note in the README about the breaking change in 2.0

# Update the example config with all available options and comments

# Fix the off-by-one error in the date range iterator
