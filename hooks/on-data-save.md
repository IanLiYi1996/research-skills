---
event: data.save
name: data-backup
description: Automatically backup and version experimental data
---

# Data Backup Hook

Automatically backup experimental data and maintain version history.

## Trigger Event
- **Event**: data.save (custom event)
- **File Types**: .csv, .json, .xlsx, .mat, .hdf5

## Actions

### Immediate Backup
1. **Create Backup Copy**:
   - Copy to `backups/` directory
   - Filename: `{original}_YYYYMMDD_HHMMSS.{ext}`
   - Preserve original file

2. **Calculate Checksum**:
   - Generate MD5 or SHA256 hash
   - Store in `checksums.txt`
   - Verify data integrity

3. **Update Metadata**:
   - Record save timestamp
   - Log file size
   - Track version number
   - Store in data manifest

### Database Update
1. Insert/update record in experiment database
2. Link to experiment ID if available
3. Record file path and backup location
4. Store metadata (size, hash, timestamp)

### Git Integration
1. Check if file is tracked in git
2. If tracked, create git commit with descriptive message
3. Tag significant versions
4. Push to remote (if configured)

## Backup Strategy

### Retention Policy
- Keep last 10 versions of each file
- Archive older versions to compressed storage
- Monthly cleanup of old backups
- Never delete last version

### Storage Structure
```
backups/
├── daily/
│   ├── data_20240101_120000.csv
│   └── data_20240101_150000.csv
├── weekly/
│   └── data_20240101_000000.csv
└── monthly/
    └── data_202401.zip
```

## Configuration

```json
{
  "hooks": {
    "data-backup": {
      "enabled": true,
      "backup_location": "./backups",
      "max_versions": 10,
      "auto_git_commit": true,
      "checksum_algorithm": "sha256",
      "compress_old": true,
      "retention_days": 90
    }
  }
}
```

## Error Handling

If backup fails:
1. Show warning notification
2. Retry backup operation
3. If still fails, log error but don't block save
4. Alert user to check backup manually

## Notes

- Ensures data safety and recoverability
- Maintains version history
- Integrates with git for version control
- Automatic cleanup prevents disk space issues
- Critical for research data management
