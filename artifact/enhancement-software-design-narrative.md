# Enhancement One: Software Design and Engineering  
## Grazioso Salvare Animal Rescue Dashboard

The artifact selected for this milestone is the **Grazioso Salvare Animal Rescue Dashboard**, originally developed in CS 340 (Client/Server Development). The project is a Python-based application that connects to a MongoDB database and displays animal rescue data through an interactive Dash dashboard.

Originally, the project demonstrated CRUD concepts primarily through Jupyter notebook workflows, with the dashboard focused on basic data retrieval and user interaction. For CS 499, I enhanced the project to better reflect professional software design, maintainability, and secure development practices.

---

## Justification for Inclusion

I selected this artifact because it represents a complete, data-driven application rather than a standalone code example. It combines:

- Backend database access  
- Application logic  
- A user-facing dashboard interface  

The project demonstrates my ability to refactor and enhance an existing system using structured engineering practices.

---

## Enhancements Implemented

### Backend Refactoring
- Centralized CRUD operations into a reusable backend module  
- Added structured error handling  
- Implemented input validation  
- Removed hardcoded credentials and replaced them with environment-based configuration  
- Enhanced read functionality to support projections  

### Project Structure Improvements
- Clearly separated original and enhanced versions  
- Added `.gitignore`  
- Added `requirements.txt`  
- Implemented smoke tests and admin CRUD tests  

### Dashboard Improvements
- Removed deprecated method calls  
- Excluded internal MongoDB fields at the query level  
- Improved layout presentation (logo centering and visual cleanup)  

---

## Learning and Reflection

These enhancements strengthened my understanding of how backend refactoring impacts dependent systems. I learned the importance of incremental validation when modifying production-style systems.

These changes reflect an **iterative SDLC approach** — refactoring in small increments, validating functionality after each change, and improving configuration management to increase maintainability while reducing regression risk.

Overall, the enhanced artifact is:

- More maintainable  
- More secure  
- Better structured  
- More suitable for professional presentation  

---

## Resources

- MongoDB, Inc. (n.d.). *CRUD operations.* MongoDB Manual.  
  https://www.mongodb.com/docs/manual/crud/

- MongoDB, Inc. (n.d.). *Project fields from query results.*  
  https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/

- Behlendorf, B., et al. (n.d.). *The Twelve-Factor App: Config.*  
  https://12factor.net/config

- Python Software Foundation. (n.d.). *Structuring your project.*  
  https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/

- Plotly Technologies Inc. (n.d.). *Dash layout.*  
  https://dash.plotly.com/layout

- OWASP Foundation. (n.d.). *Secure Coding Practices Quick Reference Guide.*  
  https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/
