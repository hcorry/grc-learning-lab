# Data Classification Procedure

**Companion to:** Data Classification Policy
**Document Owner:** CISO
**Version:** 1.0

> 📖 **Instructions:** Write the operational "how-to" for classifying and handling data. Think about what a new employee or a data owner would need to follow step by step.

---

## 1. Classifying New Data

> **✏️ YOUR WORK**
> YOUR WORK: Write the steps for determining the classification level of new data.
>
> Think about:
> - When does classification happen? (When new data is created, collected, or received)
> - Who classifies it? (The data owner — usually the business leader responsible for that data)
> - What questions determine classification?
>   - Is this data regulated by any law? (PII, financial data → likely Confidential or Restricted)
>   - What's the impact if this data were disclosed? (Low → Internal, High → Restricted)
>   - Is this data intended for public consumption? (If yes → Public)
>   - Does this data contain credentials, keys, or security info? (If yes → Restricted)
> - How is the classification recorded? (Labeling, metadata, data inventory)
> - What if you're unsure? (When in doubt, classify at the HIGHER level and ask the data owner)
>
> Write 5-7 numbered steps.

---

## 2. Labeling Classified Data

> **✏️ YOUR WORK**
> YOUR WORK: Write the steps for labeling data according to its classification.
>
> Think about different formats:
> - Digital documents: header/footer with classification level, or file naming convention (e.g., "[CONFIDENTIAL] Q4 Financial Report.pdf")
> - Emails: classification tag in subject line (e.g., "[INTERNAL] Team meeting notes")
> - Cloud storage: folder structure by classification, or labels/tags in the platform
> - Physical documents: stamps or printed headers
> - Databases: classification metadata field
>
> Write 4-6 numbered steps covering the main formats SecureTech uses.

---

## 3. Handling Data by Classification Level

> **✏️ YOUR WORK**
> YOUR WORK: Write specific procedures for each classification level. This is the most detailed section.
>
> ### Handling Public Data
> (Can be shared freely, but still should be accurate and approved before release. Write 3-4 steps.)
>
> ### Handling Internal Data
> (Keep within the organization, basic protections. Write 4-5 steps covering: storage, sharing internally, what NOT to do.)
>
> ### Handling Confidential Data
> (Encryption required, access restricted, sharing only with approval. Write 5-7 steps covering: storage, access, sharing, transmission, disposal.)
>
> ### Handling Restricted Data
> (Strictest controls — encryption everywhere, logging, limited access, no external sharing without executive approval. Write 6-8 steps.)
>
> For each level, address: Where can it be stored? How can it be shared? How must it be transmitted? How must it be destroyed?

---

## 4. Data Disposal / Destruction

> **✏️ YOUR WORK**
> YOUR WORK: Write the steps for securely disposing of data that's no longer needed.
>
> Think about:
> - How do you decide data should be disposed of? (Retention period expired, project complete, regulatory requirement)
> - Who approves disposal? (Data owner)
> - Methods by format:
>   - Digital files: secure deletion (not just "delete" — overwrite or crypto-erase)
>   - Physical documents: cross-cut shredding
>   - Storage media (hard drives, USB): physical destruction or certified wiping
>   - Cloud data: verify deletion from all locations including backups
> - How is disposal documented? (Disposal log with date, method, who performed it, who approved it)
>
> Write 5-7 numbered steps.

---

## 5. Reclassification Procedure

> **✏️ YOUR WORK**
> YOUR WORK: Write the steps for changing a data asset's classification level.
>
> Think about:
> - What triggers reclassification? (Data no longer sensitive, data becomes more sensitive, business change, regulatory change)
> - Who can request reclassification? (Anyone, but data owner approves)
> - What changes when classification changes? (Labeling, storage location, access permissions, handling requirements)
> - How is reclassification documented?
>
> Write 4-6 numbered steps.
