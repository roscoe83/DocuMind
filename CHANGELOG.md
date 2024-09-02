# Changelog


## 2024-05-23
- Bump minimum Python version to 3.10 and update type hints accordingly

## 2024-05-29
- Clean up unused imports and fix formatting to match the project style guide

## 2024-05-29
- Fix the test that was flaky due to reliance on system time

## 2024-06-04
- Correct the default value for the feature flag in production

## 2024-06-07
- Improve logging so we can trace requests through the pipeline in production

## 2024-06-10
- Implement basic rate limiting to avoid overwhelming the downstream service

## 2024-06-13
- Simplify the auth flow by using a single token source

## 2024-06-19
- Adjust default timeout value to prevent premature connection drops

## 2024-06-19
- Adjust the batch size to reduce memory usage on large inputs

## 2024-06-19
- Remove the experimental feature that didn't make it into the release

## 2024-06-22
- Support passing options through the config file as well as CLI

## 2024-06-28
- Adjust default timeout value to prevent premature connection drops

## 2024-07-04
- Correct typo in the error message shown when validation fails

## 2024-07-10
- Correct the default value for the feature flag in production

## 2024-07-19
- Improve the CLI help text so it's clear how to use each option

## 2024-07-19
- Bump the version and tag the release in the repo

## 2024-07-19
- Add integration test that covers the full flow from request to response

## 2024-07-22
- Bump the library version and pin the dependency in requirements

## 2024-07-25
- Add integration tests for the new export endpoint

## 2024-07-25
- Clean up the test fixtures and move shared data to a single file

## 2024-07-25
- Add integration test that covers the full flow from request to response

## 2024-08-06
- Bump version to 1.2.0 and add changelog entry for the new features

## 2024-08-09
- Improve performance by caching the result of the expensive lookup

## 2024-08-12
- Add a small delay between retries to avoid thundering herd

## 2024-08-15
- Bump the Docker base image to get the latest security patches

## 2024-08-27
- Support environment-specific overrides via separate config files

## 2024-09-02
- Improve performance by caching the result of the expensive lookup

## 2024-09-02
- Simplify error messages so they are actionable for the end user
