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
