# Contributing to Florist-Database

First and foremost, thank you for considering contributing to the Florist-Database project! We appreciate any help, whether it's a simple bug report, a feature request, or a code contribution. This document will guide you through the contribution process.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Reporting Bugs](#reporting-bugs)
4. [Feature Requests](#feature-requests)
5. [Code Contribution](#code-contribution)
6. [Pull Request Process](#pull-request-process)
7. [Testing](#testing)
8. [License](#license)

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct. Please report unacceptable behavior to [project maintainers' email].

## Getting Started

1. **Fork the Repository**: Click on the 'Fork' button at the top right corner of the repository page to do this. This will create a copy of the repository in your GitHub account.
2. **Clone the Repository**: Now, clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the 'Code' button, and then click the clipboard icon to copy the URL. Open your terminal and execute the following git command:

```
git clone [URL]
```

3. **Navigate to the Repository**: Use the following command to navigate to the cloned repository:

```
cd Florist-Database
```

4. **Create a New Branch**: Create a new branch using the git command:
```
git checkout -b your-new-branch-name
```


## Reporting Bugs

If you find a bug, please create an issue in the repository detailing:

- A clear and descriptive title.
- Steps to reproduce the bug.
- Expected behavior.
- Actual behavior.
- Screenshots (if applicable).
- Any other information that might be relevant.

## Feature Requests

If you have an idea for a new feature:

- Check the issues list to see if it hasn't been proposed before.
- Create a new issue with a clear and descriptive title.
- Describe the feature and why you think it would be useful.
- Add any relevant screenshots or mockups.

## Code Contribution

1. Ensure you've followed the [Getting Started](#getting-started) section.
2. Make your changes in the new branch.
3. Commit your changes using a descriptive commit message.
4. Push your changes to your forked repository on GitHub.
5. Create a new Pull Request to our master branch.

## Pull Request Process

1. Ensure that your code follows the coding conventions of the project and that you've added tests if introducing new features.
2. Update the README.md with details of changes, this includes new environment variables, exposed ports, useful file locations, and container parameters.
3. Your Pull Request will be reviewed by the maintainers. Address any comments and make necessary changes.
4. Once approved, your Pull Request will be merged into the master branch.

## Testing

Before submitting your changes, ensure that:

- All existing tests pass.
- New tests cover any new features or logic you've added.

To run tests, execute:
```
python test_florist_database.py
```
## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the main project. See [LICENSE](LICENSE) for more details.


