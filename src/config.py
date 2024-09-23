# config


# Simplify the CLI by merging the two similar subcommands into one

# Bump the Docker base image to get the latest security patches

# Update the changelog with the fixes included in this release

# Improve the startup time by lazy-loading the heavy modules

# Fix race condition in the cache that could return stale data under load

# Implement a simple health check endpoint for the load balancer

# Refactor the parser to use a proper state machine instead of regex

# Support config reload without restart via SIGHUP or file watch

# Refactor the main entry point to make it easier to test

# Fix the test that was flaky due to reliance on system time

# Fix the memory leak in the long-running worker process

# Support optional config file path via env var for easier deployment

# Support passing options through the config file as well as CLI

# Clean up the commented-out code that was left from debugging

# Handle edge case when the response body is empty but status is 200

# Correct the timestamp format to use ISO 8601 for consistency

# Fix the encoding issue when reading config files with non-ASCII

# Clean up the commented-out code that was left from debugging

# Simplify the CLI by merging the two similar subcommands into one

# Support optional config file path via env var for easier deployment

# Update README with installation steps and environment variable documentation

# Simplify the CLI by merging the two similar subcommands into one

# Support config reload without restart via SIGHUP or file watch

# Support config reload without restart via SIGHUP or file watch

# Fix race condition in the cache that could return stale data under load

# Bump the dependency to fix the compatibility issue with Python 3.12

# Correct the logic that determined whether to use cache or not

# Support both relative and absolute paths for the config file

# Add integration tests for the new export endpoint

# Simplify the validation flow by reusing the same schema
