# CodeMapper TODO List

- [ ] Add these tasks to the github project board

## Core Functionality

tag is: [`core`](https://github.com/users/shaneholloman/projects/9/views/7)

- [x] Implement direct repository URL analysis
- [ ] Expand Git hosting service support (GitLab, Bitbucket)
- [ ] Develop progress indicator for large repository processing
- [ ] Enable custom branch selection
- [ ] Implement intelligent repository categorization
  - [ ] Deterministic analysis
  - [ ] AI-powered analysis
  - [ ] Add option to update original repo with categories (for owners)
- [ ] Create config yaml file for user preferences
  - [ ] Git pull location
  - [ ] CodeMaps location
  - [ ] DocMaps location
  - [ ] Output format default
  - [ ] api keys for AI integration
  - [ ] Ai services to use

## File Outputs

tag is: [`files`](https://github.com/users/shaneholloman/projects/9/views/7)

- [x] Generate `*_codemap.md` for file contents and directory structure
- [ ] Create separate `*_docmap.md` for documentation directories
- [ ] Add repository source information to output file header

## CodeMapper Service

tag is: [`service`](https://github.com/users/shaneholloman/projects/9/views/7)

- [ ] Create a server version of CodeMapper with API
- [ ] Implement user authentication and authorization
- [ ] Ansible playbook for server deployment

## Documentation

tag is: [`docs`](https://github.com/users/shaneholloman/projects/9/views/7)

- [x] Utilize changelog.md for version tracking

## AI Integration

tag is: [`ai`](https://github.com/users/shaneholloman/projects/9/views/7)

- [ ] Implement AI-generated alt text for images --option
- [ ] Implement AI-generated code summarization --option
- [ ] Explore base64 image encoding and embedding in output --option

## Output Formats

tag is: [`outputs`](https://github.com/users/shaneholloman/projects/9/views/7)

- [x] Markdown (default)
- [ ] JSON
- [ ] YAML
- [ ] reStructuredText
- [ ] AsciiDoc

## User Experience

tag is: [`ux`](https://github.com/users/shaneholloman/projects/9/views/7)

- [ ] Create PreFlight checks for CodeMapper
  - [ ] Check for git
  - [ ] Check for Python version
  - [ ] Check for required libraries
- [ ] Create function for an install advisory for first-time users
  - [ ] Checks for git
  - [ ] Detect your OS
  - [ ] Give advise on how to install git based on OS
- [ ] Develop comprehensive help command and menu
- [ ] Enhance Table of Contents generation
  - [ ] Consider using `md_toc` library for robustness
- [ ] EPIC: Introduce Mermaid flow chart option for code execution flow visualization

## Developer Experience

tag is: [`dev`](https://github.com/users/shaneholloman/projects/9/views/7)

- [x] Implement CI for linting
- [ ] Implement CI for automated testing
- [ ] Implement CI for PyPI package deployment
