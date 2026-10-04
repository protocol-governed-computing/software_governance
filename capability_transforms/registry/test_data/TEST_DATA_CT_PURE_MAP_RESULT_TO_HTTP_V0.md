# TEST_DATA_CT_PURE_MAP_RESULT_TO_HTTP_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_MAP_RESULT_TO_HTTP_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_MAP_RESULT_TO_HTTP_V0
target: capability_transforms::CT_PURE_MAP_RESULT_TO_HTTP_V0
cases:
- case_id: success_with_data
  expected_outcome: SUCCESS
  bindings:
    execution_result:
      status: SUCCESS
      exit_reason_code: null
      trace_id: null
      result_payload:
        user_id: usr_123
        action: created
        timestamp: '2026-04-02T10:00:00Z'
    mapping:
      SUCCESS: 200
      FAILURE: 400
      ERROR: 500
  expected:
    http_status: 200
    response_body:
      status: SUCCESS
      exit_reason_code: null
      trace_id: null
      result_payload:
        user_id: usr_123
        action: created
        timestamp: '2026-04-02T10:00:00Z'
    result_status: SUCCESS
- case_id: failure_with_error
  expected_outcome: SUCCESS
  bindings:
    execution_result:
      status: FAILED
      exit_reason_code: EXIT_VIOLATION
      trace_id: null
      result_payload: {}
      error_code: VALIDATION_ERROR
      message: Invalid email format
    mapping:
      SUCCESS: 200
      VIOLATION: 400
      BACKEND_ERROR: 500
  expected:
    http_status: 400
    response_body:
      status: FAILED
      exit_reason_code: EXIT_VIOLATION
      trace_id: null
      result_payload: {}
      error_code: VALIDATION_ERROR
      message: Invalid email format
    result_status: VIOLATION
- case_id: error_with_custom_mapping
  expected_outcome: SUCCESS
  bindings:
    execution_result:
      status: FAILED
      exit_reason_code: EXIT_BACKEND_ERROR
      trace_id: null
      result_payload: {}
      error_code: INTERNAL_ERROR
      message: Database connection failed
    mapping:
      SUCCESS: 200
      VIOLATION: 400
      BACKEND_ERROR: 503
  expected:
    http_status: 503
    response_body:
      status: FAILED
      exit_reason_code: EXIT_BACKEND_ERROR
      trace_id: null
      result_payload: {}
      error_code: INTERNAL_ERROR
      message: Database connection failed
    result_status: BACKEND_ERROR
- case_id: success_empty_value
  expected_outcome: SUCCESS
  bindings:
    execution_result:
      status: SUCCESS
      exit_reason_code: null
      trace_id: null
      result_payload: {}
    mapping:
      SUCCESS: 204
      FAILURE: 400
      ERROR: 500
  expected:
    http_status: 204
    response_body:
      status: SUCCESS
      exit_reason_code: null
      trace_id: null
      result_payload: {}
    result_status: SUCCESS
- case_id: success_complex_nested
  expected_outcome: SUCCESS
  bindings:
    execution_result:
      status: SUCCESS
      exit_reason_code: null
      trace_id: null
      result_payload:
        transaction:
          id: tx_abc123
          type: transfer
          from:
            address: 0x1234...
            balance: 100
          to:
            address: 0x5678...
            balance: 200
          metadata:
            gas_used: 21000
            confirmations: 12
    mapping:
      SUCCESS: 200
      FAILURE: 400
      ERROR: 500
  expected:
    http_status: 200
    response_body:
      status: SUCCESS
      exit_reason_code: null
      trace_id: null
      result_payload:
        transaction:
          id: tx_abc123
          type: transfer
          from:
            address: 0x1234...
            balance: 100
          to:
            address: 0x5678...
            balance: 200
          metadata:
            gas_used: 21000
            confirmations: 12
    result_status: SUCCESS
- case_id: failure_validation_array
  expected_outcome: SUCCESS
  bindings:
    execution_result:
      status: FAILED
      exit_reason_code: EXIT_VIOLATION
      trace_id: null
      result_payload: {}
      error_code: VALIDATION_ERROR
      message: Multiple validation errors
    mapping:
      SUCCESS: 200
      VIOLATION: 422
      BACKEND_ERROR: 500
  expected:
    http_status: 422
    response_body:
      status: FAILED
      exit_reason_code: EXIT_VIOLATION
      trace_id: null
      result_payload: {}
      error_code: VALIDATION_ERROR
      message: Multiple validation errors
    result_status: VIOLATION
```

## Intent

Validates HTTP response mapping for various execution result statuses.

Tests cover:
- SUCCESS with data payload
- FAILURE with error message
- Custom status codes via mapping
- Empty result handling
- Complex nested data structures

---
