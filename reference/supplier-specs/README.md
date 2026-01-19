# Supplier Specifications

This folder contains product specifications, datasheets, and documentation from suppliers.

## Purpose

- Store authoritative product dimensions and specifications
- Reference source for design constraints
- Maintain traceability to supplier documentation

## File Organization

```
supplier-specs/
├── README.md                    # This file
├── habitat/                     # Habitat shell specs (Osterath)
│   └── *.pdf
├── windows/                     # Window specifications
│   └── *.pdf
├── doors/                       # Door specifications
│   └── *.pdf
├── hvac/                        # HVAC components
│   └── *.pdf
├── electrical/                  # Electrical components
│   └── *.pdf
├── plumbing/                    # Plumbing fixtures
│   └── *.pdf
└── furniture/                   # Built-in furniture specs
    └── *.pdf
```

## Naming Convention

`[supplier]-[product]-[version].[ext]`

Example: `osterath-habitat-1225AF-specs.pdf`

## Usage

1. Add supplier PDFs to the appropriate subfolder
2. Reference in habitat.yml or requirements files
3. Extract key dimensions into YAML for programmatic use

## Notes

- These files are reference-only
- Do not modify supplier documents
- If specs change, archive old version and add new
