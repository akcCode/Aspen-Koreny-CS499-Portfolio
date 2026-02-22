# Milestone Three Narrative  
## Enhancement Two: Algorithms and Data Structures  
### Grazioso Salvare Animal Rescue Dashboard

The artifact selected for this milestone is the Grazioso Salvare Animal Rescue Dashboard, originally created in CS 340 Client/Server Development. The Python-based dashboard connects to a MongoDB database containing animal shelter data from the Austin, Texas area, allowing users to filter, visualize, and explore animal records to identify dogs best suited for different search-and-rescue training roles.

I selected this artifact for my ePortfolio because it represents a complete, data-driven application rather than an isolated code example. It demonstrates how algorithms and data structures are applied in a realistic context to process, filter, and summarize data in support of user decision-making. The filtering logic that builds database queries based on selected rescue types and the aggregation logic that calculates breed frequencies for visualization highlight my ability to apply algorithmic thinking to real-world problems.

This enhancement involved moving the aggregation logic, grouping, counting, sorting, and limiting results from the application layer into MongoDB using aggregation pipelines. This shift reduces repeated computation and improves efficiency and scalability, aligning with industry best practices of handling such operations at the database level. MongoDB’s aggregation framework processes data efficiently, minimizing unnecessary data transfer and enhancing performance. Eckerson (2010) highlights that optimized backend processing is essential for effective dashboards.

In the original version, the dashboard pulled the filtered dataset into the application layer and then performed grouping and counting with pandas. That approach works, but it adds repeated client-side computation and increases data transfer as the dataset grows. By using MongoDB’s aggregation pipeline to group, count, sort, and limit results within the database, the dashboard reduces unnecessary processing in Python and scales better for larger collections.

This enhancement addressed the course outcomes from Module One related to designing computing solutions using algorithmic principles. Refactoring the breed-count calculation in the Grazioso Salvare database demonstrated an understanding of how algorithm placement affects performance and maintainability. The changes simplified the application layer and improved system structure, with no updates needed to my outcome-coverage plan.

Through this work, I learned how to choose the right system layer for algorithms. While the original pandas-based implementation functioned, it wasn’t ideal for larger datasets or scalability. Moving the logic to the database clarified the trade-offs between simplicity and efficiency. A key challenge was ensuring the aggregation pipeline's results were consistent with the original implementation. Overall, this experience reinforced how algorithms and data structures affect system performance and reliability, boosting my confidence in applying algorithmic reasoning in a full-stack application.


---

## Resources

- Eckerson, W. W. (2010). Performance dashboards: Measuring, monitoring, and managing your business (2nd ed.). John Wiley & Sons.

- MongoDB, Inc. (2024). Aggregation pipeline.  
  https://www.mongodb.com/docs/manual/aggregation/
