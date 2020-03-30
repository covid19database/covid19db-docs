# Open, opt-in, risk publishing

## Problem Statement:
There are numerous efforts to develop tools and software to help with tracing and self-isolation in response to the Covid19 crisis.  Many of these efforts are focused on mobile apps that collect geospatial time-series and BLE rendezvous events to help in the tracing process when a user tests positive and to help identify when a user is at risk of being a carrier.  The development of multiple competing mobile applications will help foster innovation and improve user experiences but also creates a fundamental problem: users are likely reporting data to only a fraction of other users who have adopted the same application.  At the same time, government entities do not have mechanisms to disseminate information about where and when people may have come in contact with the virus.

## Proposed Solution:
There is a need for a common data service where mobile apps and government entities can publish and exchange geospatial time-series.  We propose (and are developing) a service that associates publicly visible named counters to intervals of time and space that can be used to aggregate evidence (e.g., `cdc.gov/c19/positive_test`, `bleapp.stanford.edu/high_fevers`).  For example, an app may ask a user who is presenting symptoms if they are willing to publish their space-time trajectory by updating the high_fever counters at all public locations they visited in the past week.  Similarly, government entities could publish positive evidence and notifications to regions of time and space that users may have passed through.  Mobile apps can then locally track where users have been and query this service to collect and aggregate evidence of risk and any notifications associated with users past trajectories. Furthermore, experts can mine these public records to compute improved risk statistics.

## Assumptions and Limitations:
In the design of this service to exchange information, we are assuming users who test positive or are showing symptoms would be willing to (opt-in) contribute anonymously to counters in public spaces.  We are not explicitly focusing on differential privacy, MPC, or enclave technology since these are unlikely to substantially improve user confidence and at present create hurdles to large-scale short-term adoption.   Finally, by not tracking individual interactions or the background population, we will not be able to directly identify asymptomatic carriers or higher-order transmission.  

## Call for Collaboration:
We are looking to partner with each of the major app developers to help adapt our system design to their needs and to ensure that they can meaningfully exchange data using our system.  Since our strength is in the design of scalable data systems, we hope to complement the significant mobile application efforts already under development.  

## Contact us:
- Prof. Joseph Gonzalez (jegonzal@berkeley.edu)
- or just read an outline of [our system spec](docs/DESIGN.md)
