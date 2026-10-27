# Fault Code Assist beta: what we've learned so far

*Fictional. Internal product note, 6 Oct 2026.*

## What it is

When a telematics fault code arrives, Fault Code Assist explains it in plain English, rates it (act now / plan in / watch) and suggests a VMRS repair code. The maintenance manager still decides whether to open a work order and types it in. Built on a general large language model plus our fault-code library. In beta since May 2026; no charge during the beta.

## Usage

- 46 customers in the beta, out of about 310 with a telematics integration switched on.
- 31 of the 46 used it in the last 30 days.
- 5,800 fault codes explained since May. Users gave a thumbs-up to 61% and a thumbs-down to 9%; the rest weren't rated.
- 18% of "act now" codes became a work order within 24 hours. We can't yet tell if the rest were false alarms or ignored.

## What users say

- "Saves my lead tech an hour a morning on the bad days." (maintenance manager, 240-tractor carrier)
- "Tells me what the code means. I still have to do everything else." (shop supervisor, 90-truck fleet)
- "Too many 'watch' codes. Hide them unless they repeat." (maintenance manager, waste hauler)
- "If it already knows what the code is, why can't it start the work order and pull the parts?" (parts manager, beverage distributor)

## Open questions

- Pricing: include it in Pro, or charge per vehicle as an add-on?
- Can we use repair outcomes across customers to rank codes by what actually led to a breakdown? Our 2021 contract allows de-identified, aggregated data for product improvement and benchmarks; about 70% of customers are on it. Legal hasn't confirmed this covers training models.
- Accuracy: no one has checked suggestions against what technicians actually found.
