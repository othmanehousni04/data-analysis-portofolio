# Project 3: Interactive Netflix Content Dashboard

## Objective:
To analyze a messy dataset of Netflix titles, with the goal of cleaning the data and building an interactive dashboard to identify content trends.

## Tools Used:
* **Power BI**
* **Power Query** (for data cleaning)
* **DAX** (for `IF` logic, though not used in this one)

## What I Did (My Process):
1.  **Data Cleaning (Power Query):** This was the biggest challenge. The raw data was messy.
    * Cleaned inconsistent `genres` data (`['drama', 'crime']`) by splitting, replacing, and **unpivoting** the columns to create a single, usable "Genre" column.
    * Cleaned "dirty" text by using **Trim** and **Clean** to remove hidden spaces.
    * **Filtered** out all `(Blank)` and `null` values to create a clean, usable dataset.
2.  **Data Visualization (Power BI):**
    * Built a "Top 10 Genres" chart by counting the new, unpivoted genre data.
    * Created a "Top 10 Rated Movies" table using a **Top N filter**.
    * Added a line chart for content releases over time and a donut chart for the MOVIE/SHOW split.
    * Created a "Top 10 Production Countries" chart using a **Top N filter**.
3.  **Dashboard Design:**
    * Designed a clean, professional "dark mode" dashboard.
    * Used shadows, clean titles, and slicers to make the report fully interactive.

<img width="1448" height="815" alt="image" src="https://github.com/user-attachments/assets/6862d77d-8545-41ed-a5ec-bcce6088c398" />
<img width="1445" height="814" alt="image" src="https://github.com/user-attachments/assets/91d7653f-bf66-4812-a633-ffe5965f7cba" />
<img width="1445" height="813" alt="image" src="https://github.com/user-attachments/assets/59e9ef23-2a47-421b-b59d-d36fa4f796f2" />
