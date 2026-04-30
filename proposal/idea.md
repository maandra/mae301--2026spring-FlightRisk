# 1. Project **Flight Risk**


# 2. Team Members (names, emails)
  - Melissa Andrade, maandra9@asu.edu
  - William Jones, whjones3@asu.edu
  - Gary Nez, gwnez@asu.edu
  - Janine Nelson, jenels19@asu.edu
  - Lariella Citron, lcitron@asu.edu
    
# 3. Problem Statement
Have you ever had your plans thrown off because your flight was unexpectedly cancelled? Our nanoGPT model, **Flight Risk**, will estimate the probability of a flight being delayed or cancelled so users can plan their trips more effectively around possible disruptions.

- **Who is the user?**  
  Anyone who expects to fly on a commercial airline flight, as well as anyone whose plans may be affected by flight delays or cancellations.

- **What problem or pain point do they experience today?**  
  Flights are delayed or cancelled every day, often with little warning. These disruptions can negatively affect business trips, vacations, and family travel.

# 4. Why Now?
AI models now have the ability to process large amounts of data and make more accurate predictions than ever before. This problem matters in the next 3–5 years because air travel demand remains high, disruptions are common and costly, and travelers increasingly care about reliability before they book.

Several changes make this product more possible today than it was a few years ago. Aviation data infrastructure is improving, with the FAA modernizing how aeronautical data is collected and shared to support real-time operations. In addition, AI tools are now strong enough to detect patterns across interacting variables such as weather, route history, airport congestion, and airline performance.

# 5. Proposed AI-Powered Solution
- **What does your product do for the user?**  
  Our model gives users insight into the probability that their flight will be delayed or cancelled. By knowing there is a higher chance of delay, a traveler can adjust plans ahead of time. For example, someone picking up a friend from the airport may need to also be at work shortly after. If the flight is likely to be delayed, they can make a better plan in advance instead of being forced into a last-minute conflict.

- **Where does AI/ML add unique value vs. simple rules/heuristics?**  
  The reasons flights are delayed can change over time. Weather is one of the biggest causes of delays and cancellations, and increasingly severe weather may make disruptions more common. AI is more useful than fixed heuristics because it can adapt as new data becomes available and learn changing patterns over time.

# 6. Initial Technical Concept
- **What data would you need (or already have)?**  
  Our initial datasets contain information for millions of flights between **2018–2022**. These include features such as date, airline, origin, destination, cancelled (true/false), diverted (true/false), scheduled departure time, actual departure time, departure delay minutes, arrival time, arrival delay minutes, air time, scheduled elapsed flight time, actual flight time, distance, day of the month, day of the week, operating airline, and more.

  We also plan to add storm-related data to improve weather-based predictions. This dataset includes storm date, time, and state information from **1950–2015**.

- **What model(s) might you use?**  
  We plan to use **classifier models** for this project. The classifier will predict the probability of a flight being:
  - **On time**
  - **Short delay** (< 30 minutes)
  - **Long delay** (> 30 minutes)
  - **Cancelled**

- **How could your nanoGPT work feed into this?**  
  Our nanoGPT work could support the project by helping explain results to users in a clear way, summarizing risk factors behind a prediction, or generating user-friendly travel guidance based on the model’s output.

# 7. Scope for MVP
- **What can you realistically build in ~6 weeks?**  
  In about 6 weeks, a realistic MVP is a **flight reliability ranking tool**, not a full booking or real-time disruption platform.

- **Define a very concrete v1 feature:**  
  A user can enter an **origin, destination, and travel date**, and our system returns a **ranked list of flight options by likelihood of delay or cancellation**, using historical on-time performance and a small set of current factors such as route, airline, departure time, and weather forecast if available.

# 8. Risks and Open Questions
- **Top 3 unknowns**
  1. **Timely Data:** Historical flight data is easier to obtain, but current data is harder to access. Older data may be less reliable for modern flight predictions.
  2. **Irregular Operations:** Storms, strikes, and other unusual disruptions could make the algorithm less reliable because these events may not appear often enough in the training data.
  3. **Changing Operations:** Airlines and airports change their operating patterns over time, so the model may need regular updates to remain accurate.

# 9. Planned Data Sources
We plan to use **Kaggle** to source our datasets. We have already downloaded datasets that include thousands of flight records from **2018–2022**. These datasets include information such as cancellation status, delayed departure and arrival times, flight origin and destination, airline, and other related flight details.
