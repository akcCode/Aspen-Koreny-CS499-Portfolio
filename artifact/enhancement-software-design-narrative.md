# Enhancement 1: Software Design and Engineering
Milestone Two Narrative | Enhancement One: 
Software Design and Engineering
For this milestone, I enhanced the Grazioso Salvare Animal Rescue Dashboard, originally created in CS-340 (Client/Server Development). The project is a Python-based application that connects to a MongoDB database and displays animal rescue data through an interactive Dash dashboard. Originally, the project demonstrated CRUD concepts primarily through Jupyter notebook workflows, with the dashboard focused on basic data retrieval and user interaction. For CS 499, I improved the project to better reflect professional software design, maintainability, and secure development practices.
I selected this artifact for my ePortfolio because it represents a complete, data-driven application rather than a standalone code example. It combines backend database access, application logic, and a user-facing interface, making it a strong example of real-world software design. The project showcases my ability to organize code into reusable components, integrate multiple technologies, and enhance an existing system through thoughtful refactoring.
The main focus of this enhancement was the backend CRUD module. While the original project implemented CRUD functionality in a learning context, these operations were not structured as a centralized, reusable backend component. For this enhancement, the CRUD logic was refactored and expanded into a standalone module that cleanly supports create, read, update, and delete operations. Input validation and structured error handling were added to improve the reliability and predictability of database interactions. The read functionality was enhanced to support projections, allowing the dashboard to retrieve only the data it needs. Hardcoded database credentials were removed and replaced with environment-based configuration to improve security and flexibility.
In addition to backend improvements, I reorganized the project structure to follow common software engineering practices. Original and enhanced code were clearly separated, and supporting files such as a .gitignore and requirements.txt were added. A smoke test and an admin CRUD test were created to verify database connectivity and confirm the correct behavior of the enhanced backend in a local development environment.
The dashboard was updated to work with the enhanced backend and to improve overall reliability. Internal MongoDB fields were excluded at the query level, deprecated method calls were removed, and the application was configured to run consistently in a local development setup. Minor interface improvements were also made, including centering the application logo above the title to create a cleaner, more professional layout.
These enhancements support the course outcomes identified in Module One, particularly in the areas of software design, engineering practices, and secure development. This milestone strengthened my understanding of how backend changes affect dependent components and reinforced the importance of testing and incremental validation when modifying an existing system. These changes reflect an iterative SDLC approach, refactoring in small increments, validating behavior after each change, and improving configuration management to increase maintainability while reducing regression risk. Overall, the enhanced artifact is more maintainable, more secure, and better suited for inclusion in a professional ePortfolio.

















Resources
MongoDB, Inc. (n.d.). CRUD operations. MongoDB Manual.
https://www.mongodb.com/docs/manual/crud/
MongoDB, Inc. (n.d.). Project fields from query results. MongoDB Manual.
https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/
Behlendorf, B., et al. (n.d.). The twelve-factor app: Config.
https://12factor.net/config
Python Software Foundation. (n.d.). Structuring your project. Python Packaging User Guide.
https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
Plotly Technologies Inc. (n.d.). Dash layout. Dash Documentation.
https://dash.plotly.com/layout
OWASP Foundation. (n.d.). Secure coding practices quick reference guide.
https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/
