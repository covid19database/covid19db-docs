# Universal Data Service for Covid Risk Assessment

## Problem Statement:
There are numerous efforts to develop tools and software to help with contact tracing in response to the Covid19 crisis. The development of multiple competing approaches to tracing will help foster innovation and improve user adoption but also creates **two fundamental problems**. (1) If tracing is fragmented into their separate user networks it is of little value.  (2) actionable risk assessments need to be obtained and communicated while maintaining an appropriate level of individual privacy. We need a common data service where mobile apps, health services, and government entities can publish, query and exchange relevant geo-temporal data associated with the risk of coronavirus transmission.

## Proposed Solution:
We propose creating a **universal data service** that associates infection-related data with intervals of time and space in a manner that can be used to aggregate evidence of transmission risk for individuals.  **Individuals are able to query this data service to easily understand their risk of exposure based on personal mobility data that never leaves their phone.**   Government entities and health services can publish confirmed evidence and notifications to regions of time and space allowing apps to query the past and collect notifications for users.  Further, individuals can also publish relevant unconfirmed evidence (e.g., symptomatic or diagnosed, but not confirmed) at a user-determined level identity revelation (e.g., granularity space-time) as well as the level of confirmation is used for their queries.  This common data infrastructure will enable a better understanding of the disease spread and aid in the planning and management of scarce healthcare resources.  We seek to engage the broad ecosystem of application and tracing service development, as well as health providers.

## Call for Collaboration:
We are looking to partner with each of the major app developers to help adapt our system design to their needs and to ensure that they can meaningfully exchange data using our system.  Since our strength is in the design of scalable data systems, we hope to complement the significant mobile application efforts already under development.  

## Contact us:
- Prof. Joseph Gonzalez (jegonzal+covidb@berkeley.edu)
- Dr. K. Shankari (shankari@berkeley.edu)
- Johann Schleier-Smith(jssmith@berkeley.edu)
- Nathan Pemberton (nathanp@berkeley.edu)
- Alvin Wan (alvinwan@berkeley.edu)
- or just read an outline of [our system spec](docs/DESIGN.md)
