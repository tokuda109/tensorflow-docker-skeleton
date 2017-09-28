
## <a name="commit"></a> Commit message format

Each commit message consists of a header and a body. The header has a special format that includes a type, a scope and a subject:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
```

The header is mandatory and the scope of the header is optional.

Any line of the commit message cannot be longer 100 characters! This allows the message to be easier to read on GitHub as well as in various git tools.

### Type

Must be one of the following:

* **fix**: A bug fix
* **refactor**: A code change that neither fixes a bug nor adds a feature

### Scope

The scope should be the name of the npm package affected (as perceived by person reading changelog generated from commit messages.

The following is the list of supported scopes:

* readme
* tasks

### Subject

The subject contains succinct description of the change:

* don't capitalize first letter
* no dot (.) at the end

### Body

Just as in the subject, use the imperative, present tense: "change" not "changed" nor "changes". The body should include the motivation for the change and contrast this with previous behavior.
