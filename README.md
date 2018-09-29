# book-library-web-service-hufflepuff
CS5500 Book Library Web Service Project by Divya Agarwal & Krishna Karanam

## Background
I have an enormous collection of books; I'm also really particular about keeping them organized and discoverable. I want to be able to lend them to people for some period of time, know where they are and remind people to return them to me on time. I need a way to help me find books by author, subject, time period and even be able to possibly add some personal notes about the book.

## Use cases
As a user, I want to be able to:

1. Add, remove, and update books in my library
2. Find books by a particular author
3. Find all books published in a given date range
4. Find books on a certain subject or genre (i.e scientific books, sci-fi, horror, reference)
5. Group books together into lists (i.e "my favorite sci-fi books of 2016")
6. Combine any of the above to create a more complex search query (i.e all horror books published by Stephen Hawking between 1815 and 1820)
7. Mark a book as "loaned out" to an individual
8. Remind the individual I loaned my book to that they need to return it by some date I've chosen
9. Add, remove or update notes about a particular book for later reference
10. See which books are loaned out and to whom; also see whether they have returned them on time or not

# What you need to build
Your team needs to build a web-service that presents an API exposing these features. This does not require building a web interface on top of it; though that should definitely be a possible consumer of your API. To that end, you need to come up with a reasonable set of APIs that a developer can call using HTTP. This API needs to be able to accept and return JSON data for ease of inter-operation with other systems since that is a widely accepted data format these days. In addition it should have proper documentation so that any developer can write an API client or interfaces for this service.

## Tools and technologies
We will be using the following tools this semester:
Python
Flask (simple web framework)
Sphinx (for overall documentation)
PostgreSQL (for data storage)
Heroku (for deployments)
Bitbucket (for source control)
Swagger (for API documentation)
JSON (for API interoperability)
Heroku

## Deliverables
A functional and deployed API that manages to enable the user stories listed above. In addition to the functional service you need to provide documentation (the details of which we will cover later) both for your service at a high level as well as for your API (expectations, behavior, responses).
