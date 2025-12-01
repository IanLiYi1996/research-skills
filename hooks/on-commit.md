---
event: git.pre-commit
name: research-validator
description: Validate research files before git commits
---

# Research Validator Hook

Validate research files and data integrity before committing to git.

## Trigger Event
- **Event**: git.pre-commit

## Validations

### Academic Papers (.md, .tex, .docx)
- [ ] No TODO/FIXME markers in main text
- [ ] All citations have bibliography entries
- [ ] All figures referenced exist in repository
- [ ] No placeholder text (e.g., "[INSERT]", "TBD")
- [ ] Bibliography is properly formatted

### Data Files (.csv, .json, .xlsx)
- [ ] Files are valid and parseable
- [ ] No obvious sensitive data (check patterns)
- [ ] File sizes within reasonable limits
- [ ] Schema consistency (if applicable)
- [ ] No missing required columns

### Code Files (.py, .r, .js, .m)
- [ ] No debugging print statements left in
- [ ] No hardcoded paths or credentials
- [ ] Basic syntax is valid
- [ ] Required dependencies documented
- [ ] Documentation/comments updated

### Experiment Records
- [ ] Experiment IDs are properly formatted
- [ ] Required metadata fields present
- [ ] Data files referenced exist
- [ ] No incomplete entries

## Actions on Failure

1. Display specific validation errors
2. Block commit (require --no-verify to override)
3. Provide suggestions for fixes
4. Log validation results

## Configuration

```json
{
  "hooks": {
    "research-validator": {
      "enabled": true,
      "strict_mode": false,
      "check_papers": true,
      "check_data": true,
      "check_code": true,
      "check_experiments": true
    }
  }
}
```

## Bypass

Use `git commit --no-verify` to skip validation when necessary (not recommended).

## Notes

- Helps maintain research quality
- Prevents committing incomplete work
- Ensures reproducibility standards
- Can be configured per project
