# Rate Limit Core Function

## Requirements

- Ensuring resistance against Brute Force Attacks & DDOS attacks.
- Able to be deployed in a cluster model & only executing on the API gateway instance.

## Translations

- 

## Design

- There are several components that should appear in the overall architecture of the rate limiting components

    - Rules Storage: Define the rules (how many requests per seconds, rules for each components...)
    - Identifier & Status Storage: To deploy rate limit service on cluster model, every instance should have a shared storage to check the current status of a request based on its identifier. Should be implemented using a key-value based storage like Redis.
    - Rate Limit Core Functions: Handle the logic behind the rules & active status, decide whether a request should go through or not.

## Implementation

- Rate limiting function should be upgraded from the solution in the 1st part as such solution is not efficient in terms of memory and time complexity (both are O(n) and can be a burden with a large number of requests). So the algorithm would be a more greedy-like solution which would have the complexity of O(1) and 