data-ingestion-project
======================

## Prompt

Design the architecture diagram for the problem statement

## Datasets

[Film_Locations_in_San_Francisco](https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am)

[Park_Scores_2005-2014](https://data.sfgov.org/Culture-and-Recreation/Park-Scores-2005-2014/fjq8-r8ws)

[Privately_Owned_Public_Open_Spaces](https://data.sfgov.org/Culture-and-Recreation/Privately-Owned-Public-Open-Spaces/65ik-7wqd)

[Recreation_and_Parks_Properties](https://data.sfgov.org/Culture-and-Recreation/Recreation-and-Parks-Properties/gtr9-ntp6)

## Problem Statement

Department of Parks and Recreation of San Francisco decided to have a film-lover festival hosted. They hired you to architect a system that would support the website for the festival. You need to dig through some datasets they have assembled over the years that include info about the parks they oversee. You also have received some privately owned park information that is open to the public, the department wants to collaborate with those private entities in hosting the festival. You will also have to ingest data from private sources along with the provided public data. The festival organization committee would also like to track if there was a movie filmed at any of the parks / locations they oversee to host special movie showings and tours. Don’t forget there are ratings attached to each of the parks that they have been tracking over the years.

Few things to create track of before diving into design:

- Look through the data and make notes of which datasets and which columns could be useful for the department of parks and recreation’s film-lover festival database.
- After you have identified those above, clean, trim, and adjust the data as needed.
- Set up the database and populate it with the clean data.

## Install package

With a virtural environment activated, navigate to the `data-ingestion-project` directory and install the `sf-parks` package with the following command:

```bash
pip install -v .
```

## Usage

The package will expose the `sf-parks` command line tool that will assist in managing a local sqlite database. 

 - `--db`  or  `--database`: Provide a command, either `create` or `destroy` to stand up or tear down the database
 - `--d`  or  `--data`: Provide either `all` to load all four datasets into SQL tables or provide a name of a dataset to load only the data for that table. These tables should be snake cased and constrained to the following four options:
    + `film_locations`
    + `park_scores`
    + `private_open_spaces`
    + `properties`

## Example: 

To create the database and populate all tables, run the following command:

```bash
sf-parks --db create --data all
```