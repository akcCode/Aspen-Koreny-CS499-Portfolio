# Enhancement Two: Algorithms and Data Structures  
## Grazioso Salvare Animal Rescue Dashboard

The artifact selected for this milestone is the **Grazioso Salvare Animal Rescue Dashboard**, originally developed in CS 340. The Python-based dashboard connects to a MongoDB database containing animal shelter data from Austin, Texas and allows users to filter and visualize records.

---

## Justification for Inclusion

This artifact demonstrates how algorithms and data structures operate in a real-world application. It highlights:

- Dynamic query construction based on rescue type selection  
- Aggregation logic for calculating breed frequencies  
- Data transformation to support visualization  

It reflects practical algorithmic reasoning within a full-stack system.

---

## Enhancement Overview

The primary enhancement involved moving aggregation logic from the application layer (pandas) into MongoDB using aggregation pipelines.

### Original Approach
- Retrieved filtered dataset into Python  
- Performed grouping and counting using pandas  
- Increased client-side computation  
- Increased data transfer overhead  

### Enhanced Approach
- Used MongoDB aggregation pipeline  
- Grouped, counted, sorted, and limited results at the database level  
- Reduced unnecessary data transfer  
- Improved scalability  

In the original version, grouping and counting were performed after retrieving data into Python. While functional, this approach becomes inefficient as datasets grow.

By leveraging MongoDB’s aggregation framework, operations are executed within the database engine, improving efficiency and scalability while simplifying application-layer logic.

---

## Learning and Reflection

This enhancement reinforced key algorithmic principles:

- Placement of computation affects performance  
- Backend processing reduces client overhead  
- Architectural decisions influence scalability  

A key challenge was ensuring pipeline results matched the original implementation’s output. This required iterative validation and testing.

This milestone strengthened my ability to apply algorithmic reasoning in distributed systems and reinforced the trade-offs between simplicity and efficiency.

---

## Resources

- Eckerson, W. W. (2010). *Performance dashboards: Measuring, monitoring, and managing your business (2nd ed.).* John Wiley & Sons.

- MongoDB, Inc. (2024). *Aggregation pipeline.*  
  https://www.mongodb.com/docs/manual/aggregation/
