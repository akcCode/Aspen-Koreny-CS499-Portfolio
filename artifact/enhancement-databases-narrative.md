# Milestone Four Narrative  
## Enhancement Three: Databases  
### Grazioso Salvare Animal Rescue Dashboard

The artifact selected for this milestone is the Grazioso Salvare Animal Rescue Dashboard, originally created in CS 340 Client/Server Development. This Python-based dashboard connects to a MongoDB database containing animal shelter data from the Austin, Texas area and allows users to filter and visualize records to support search-and-rescue training decisions. This artifact was enhanced throughout the capstone course to better reflect professional database design, security considerations, and real-world usage.

I selected this artifact for my ePortfolio because it demonstrates practical database interaction within a complete application rather than isolated examples. For Milestone Four, the focus was on improving how data is accessed, managed, and protected. The primary enhancement was the separation of read-only dashboard access from administrative database operations. The dashboard remains read-only for standard users, while a separate admin-only command-line tool was implemented to handle create, update, and delete operations.

This design follows the principle of least privilege by limiting database write access to controlled administrative workflows rather than exposing it through the user interface. Database configuration was also externalized using environment variables instead of hardcoded credentials, improving security and maintainability. Input validation and safeguards against destructive operations were added to reduce the risk of accidental data loss. Separating read-only access from administrative writes reduces the application’s attack surface and aligns with least-privilege guidance commonly emphasized in OWASP and NIST security recommendations.

This enhancement met the course outcomes planned in Module One, particularly those related to implementing secure and effective database solutions. Separating administrative access from user-facing functionality demonstrates an understanding of database security, access control, and system design trade-offs. The enhancement also supports a broader security mindset by anticipating potential misuse and mitigating risks through architectural decisions.

Through this process, I learned that effective database design extends beyond queries and schemas to include thoughtful access control and responsibility boundaries. While allowing full CRUD access through a single interface may be simpler, separating administrative workflows results in a more secure and maintainable system. This milestone strengthened my confidence in designing database-backed applications that align with industry best practices and real-world expectations.

---

## Resources

- Bass, L., Clements, P., & Kazman, R. (2022). Software architecture in practice (4th ed.). Addison-Wesley.

- MongoDB, Inc. (2024). MongoDB security checklist.  
  https://www.mongodb.com/docs/manual/security/

- National Institute of Standards and Technology. (2023). Security and privacy controls for information systems and organizations (SP 800-53 Rev. 5).  
  https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final

- OWASP Foundation. (2023). OWASP Top 10: A04 – Insecure design.  
  https://owasp.org/Top10/
