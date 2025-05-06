# Security Policy

## Supported Versions

We currently support the following versions of this project with security updates:

| Version | Supported          |
|---------|--------------------|
| 1.x     | ✅ Yes              |
| <1.0    | ❌ No               |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please follow these steps:

1. **Do not create a public GitHub issue.**
2. Email the maintainer directly at [contact@jayakishan.com](mailto:contact@jayakishan.com) with the subject **"Security Vulnerability Report - Telco Churn Project"**.
3. Include a detailed description of the issue, reproduction steps, and potential impact.

We will:

- Acknowledge receipt within 48 hours.
- Provide a resolution or mitigation plan within 7 business days, depending on the severity.
- Credit you for the discovery, if desired.

## Security Best Practices Followed

- Only safe and widely-used libraries are used (e.g., `xgboost`, `scikit-learn`, `pandas`).
- No sensitive user data is collected or stored.
- The project avoids insecure file writes and unsafe code execution.
- Trained models and plots are stored in isolated output directories (`/outputs`).

## Disclaimer

This project is for educational and demonstration purposes. It is not production-grade software and should not be used to make real business decisions without validation and appropriate security hardening.