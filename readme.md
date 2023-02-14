# Sitemap Indexer
Sitemap Indexer is a Python project that allows for bulk indexing of pages from an XML sitemap to Google using Google's Indexing API.

The Indexing API allows for immediate indexing of pages by Google, bypassing the traditional crawling process. This can be useful for sites with a large number of pages or frequently changing content that needs to be indexed quickly.

The tool takes an XML sitemap as input and indexes all the URLs contained within it, with the option to specify a maximum number of URLs to index. The project is built on top of the official Google Cloud client libraries and requires a Google Cloud project and authentication credentials for the Indexing API.

Sitemap Indexer is a powerful tool for site owners and developers who need to ensure their content is quickly and efficiently indexed by Google.

## Using this tool
1. Clone the repo
2. Install the dependencies
3. Download service worker config in JSON format and put in the project directory with the name "worker_oath.json"
4. Put your site's sitemap URL in the config.py file.
5. Run the main file using python 3.8+

## Limits
200 URLs/day limit by indexing API for all new sites. The limit is usually increased after weeks/months of use. It's not guaranteed that the limit would increase in future but it usually does if you have a genuine case of mass indexing manually.