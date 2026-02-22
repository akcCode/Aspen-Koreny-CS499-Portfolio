# Enhancement Three: Databases  
## Grazioso Salvare Animal Rescue Dashboard

The artifact selected for this milestone is the **Grazioso Salvare Animal Rescue Dashboard**, originally developed in CS 340. This Python-based dashboard connects to a MongoDB database and supports data filtering and visualization for search-and-rescue training decisions.

---

## Justification for Inclusion

This artifact demonstrates practical database integration within a complete application rather than isolated queries. The focus of this milestone was improving:

- Access control  
- Security posture  
- Configuration management  
- Architectural separation of responsibilities  

---

## Enhancement Overview

### Separation of Responsibilities
- Dashboard restricted to read-only operations  
- Administrative CRUD functionality moved to a separate CLI tool  
- Reduced risk of unintended data modification  

### Security Improvements
- Externalized database configuration via environment variables  
- Removed hardcoded credentials  
- Added input validation  
- Added safeguards against destructive operations  

Separating read-only access from administrative writes reduces the application’s attack surface and aligns with least-privilege guidance emphasized by OWASP and NIST.

---

## Learning and Reflection

This milestone reinforced that database design includes:

- Access boundaries  
- Responsibility separation  
- Anticipating misuse  
- Designing defensively  

Although combining CRUD functionality into one interface would have been simpler, separating administrative workflows created a more secure and maintainable architecture.

This enhancement strengthened my security mindset and improved my understanding of database-backed system design in professional environments.

---

## Resources

- Bass, L., Clements, P., & Kazman, R. (2022). *Software architecture in practice (4th ed.).* Addison-Wesley.

- MongoDB, Inc. (2024). *MongoDB security checklist.*  
  https://www.mongodb.com/docs/manual/security/

- National Institute of Standards and Technology. (2023). *Security and privacy controls for information systems and organizations (SP 800-53 Rev. 5).*  
  https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final

- OWASP Foundation. (2023). *OWASP Top 10: A04 – Insecure design.*  
  https://owasp.org/Top10/
