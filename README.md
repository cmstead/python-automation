# Python Automation #

Little automations for making a big difference in Python development ease

Cookiecutter templates are in `./templates`

Snippets can be copied from `./python.json`

## Cookiecutter Templates ##

### Installation ###

#### Cookiecutter Installation ####

The templates in this project are built against the Cookiecutter code generation system. To use them, be sure you install Cookiecutter:

Check and meet all prerequisites. **DON'T FORGET TO SET YOUR PATHS CORRECTLY**

[Cookiecutter Prerequisites](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html#prerequisites)

After this, follow the installation instructions:

[Cookiecutter Installation](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html#install-cookiecutter)

#### Template Installation ####

Place templates folder in an easy-to-refer-to directory on your computer. (Mine are in ~/Documents/templates)

### Usage ###



## VS Code Snippets ##

### Installation ###

These snippets are designed to simply be copied and pasted into the VS Code Python snippets file.

1. Open the command pallette: press F1
2. Select 'Preferences: Configure User Snippets'
3. Select 'python.json'
4. Copy the contents from python.json **in this repository** and paste it into python.json **in VS Code**

### Use ###

1. Start typing an identifier (see below)
2. Select the snippet you want from the context menu that appears
3. Tab through the template, filling in the blanks and placeholders

* Note: templates will attempt to normalize your identifiers (variable and function names) to PEP 8 standard.

**Currently included snippets**

- `var` -- Variable
- `const` -- Constant
- `function` -- Function
- `class-extended` -- Class
- `ctor` -- Constructor
- `method` -- Method
- `di-class` -- Class with DI factory