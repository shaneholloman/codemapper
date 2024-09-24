# CodeMapper TODO List

## Core Functionality

- [x] Implement direct repository URL analysis
- [ ] Expand Git hosting service support (GitLab, Bitbucket)
- [ ] Develop progress indicator for large repository processing
- [ ] Enable custom branch selection
- [ ] Implement intelligent repository categorization
  - [ ] Deterministic analysis
  - [ ] AI-powered analysis
  - [ ] Add option to update original repo with categories (for owners)

## CodeMapper Service

- [ ] Create a server version of CodeMapper with API
- [ ] Implement user authentication and authorization

## Documentation

- [x] Utilize changelog.md for version tracking
- [ ] Create separate `*_docmap.md` for documentation directories
- [ ] Add repository source information to output file header

## AI Integration

- [ ] Implement AI-generated alt text for images
- [ ] Explore base64 image encoding and embedding

## Output Formats

- [x] Markdown (default)
- [ ] JSON
- [ ] YAML
- [ ] reStructuredText
- [ ] AsciiDoc

## User Experience

- [ ] Develop comprehensive help command and menu
- [ ] Enhance Table of Contents generation
  - [ ] Consider using `md_toc` library for robustness
- [ ] EPIC: Introduce Mermaid flow chart option for code execution flow visualization

## Developer Experience

- [x] Implement CI for linting
- [ ] Implement CI for automated testing
- [ ] Implement CI for PyPI package deployment

## File Handling

- [x] Generate `*_codemap.md` for file contents and directory structure
