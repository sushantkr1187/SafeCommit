# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by **Keep a Changelog**, and this project follows **Semantic Versioning**.

---

## [1.0.1] - 2026-07-31

### Added

- Added detection for AWS Secret Access Keys.
- Added support for Stripe **test** secret keys.
- Added support for Stripe **test** restricted keys.
- Added detection for GitLab Personal Access Tokens.
- Added detection for PyPI API Tokens.
- Added detection for npm Access Tokens.
- Added detection for Hugging Face Access Tokens.
- Added detection for Anthropic API Keys.
- Added detection for Groq API Keys.
- Expanded hardcoded secret detection to support variables such as `JWT_SECRET`, `CLIENT_SECRET`, `API_SECRET`, and `APP_SECRET`.
- Improved detection for hardcoded API key variables.
- Improved detection for hardcoded token variables.
- Added comprehensive demo repositories for multi-language testing.
- Added automated test cases and benchmark datasets.

### Changed

- Improved Stripe key detection to recognize both **live** and **test** credentials.
- Refined AWS secret detection to reduce false positives.
- Reduced duplicate reporting for private keys.
- Improved project documentation.
- Updated README with installation, usage examples, supported secret types, and project roadmap.
- Updated project metadata and package information.
- Improved repository structure for testing and future development.

### Fixed

- Fixed multiple edge cases in secret detection patterns.
- Improved regex accuracy for variable-based secret detection.
- Reduced false negatives across supported credential formats.

---

## [1.0.0] - 2026-07-05

### Added

- Initial public release.
- Cross-platform command-line interface.
- Recursive directory scanning.
- Detection of common API keys.
- Detection of database connection strings.
- Detection of hardcoded passwords and secrets.
- Detection of JWTs and Bearer tokens.
- Detection of private keys and certificates.
- Rich-powered terminal output.
- Lightweight regex-based scanning engine.
- PyPI package distribution.
