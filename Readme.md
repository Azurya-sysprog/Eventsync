# EventSync README

## Overview

Welcome to EventSync, a powerful and user-friendly program designed to streamline event management through data retrieval, Google Calendar integration, and intuitive event color-coding. This project was developed as part of a hackathon, and we're excited to present a solution that simplifies the often complex task of organizing and scheduling events.

## Features

### 1. Data Retrieval

EventSync excels at retrieving event information from a simulated database. The structured database is formatted as an Excel spreadsheet and includes essential details such as Name, Description, Start Date, and End Date. This ensures that the program has access to crucial event information, facilitating efficient organization and scheduling.

### 2. Google Calendar Integration

Our program seamlessly integrates with the Google Calendar API, allowing for the automatic creation of events on the user's Google Calendar. This integration ensures accuracy and efficiency in scheduling, as events are directly synced with the user's preferred calendar application.

### 3. Event Color-Coding

To enhance the user experience and streamline event planning, EventSync incorporates a sophisticated color-coding system. This intuitive feature categorizes events based on their proximity to the current date:

- Events scheduled within the next 3 days are marked in **red**.
- Events falling within a 3 to 5-day window are highlighted in **yellow**.
- Events scheduled more than 5 days in advance are denoted in **blue**.

This visual representation allows users to quickly assess and prioritize their upcoming events, facilitating efficient time management and planning.

## Getting Started

To get started with EventSync, follow these steps:

1. Clone the repository from the [hackathon project link](https://devpost.com/software/eventsync-a61cmw).
2. Install the required dependencies as specified in the project documentation.
3. Set up the simulated database with your event information in the provided Excel spreadsheet.
4. Configure the Google Calendar API integration by following the instructions in the project documentation.

## Usage

Once set up, EventSync can be executed to retrieve data from the simulated database, integrate with the Google Calendar API, and display color-coded events for efficient planning.

```bash
# Run the program
python eventsync.py
```

## Contributing

We welcome contributions to enhance the functionality and features of EventSync. If you have ideas, bug fixes, or improvements, feel free to open an issue or submit a pull request on the project's [GitHub repository](https://github.com/yourusername/eventsync).

## License

EventSync is released under the [MIT License](LICENSE), granting users the freedom to modify and distribute the software.

Thank you for choosing EventSync! We hope this tool makes your event planning experience more enjoyable and efficient. If you encounter any issues or have suggestions for improvement, please don't hesitate to reach out.

Happy event organizing!
