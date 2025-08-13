from scihub import SciHub
import re
import os
import urllib3
import requests

# Disable HTTPS certificate verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def create_scihub_instance():
    """Create and configure SciHub instance"""
    sh = SciHub()
    sh.timeout = 90  # Increase timeout to 90 seconds
    return sh

def search_paper_by_doi(doi):
    """Search for a paper on Sci-Hub using DOI"""
    sh = create_scihub_instance()
    try:
        result = sh.fetch(doi)
        return {
            'doi': doi,
            'pdf_url': result['url'],
            'status': 'success',
            'title': result.get('title', ''),
            'author': result.get('author', ''),
            'year': result.get('year', '')
        }
    except Exception as e:
        print(f"Search error: {str(e)}")
        return {
            'doi': doi,
            'status': 'not_found'
        }

def search_paper_by_title(title):
    """Search for a paper on Sci-Hub using title"""
    # Since SciHub package doesn't support search method, we use DOI search instead
    # First try to get DOI from CrossRef
    try:
        url = f"https://api.crossref.org/works?query.title={title}&rows=1"
        response = requests.get(url, timeout=90)
        if response.status_code == 200:
            data = response.json()
            if data['message']['items']:
                doi = data['message']['items'][0]['DOI']
                return search_paper_by_doi(doi)
    except Exception as e:
        print(f"CrossRef search error: {str(e)}")
    
    return {
        'title': title,
        'status': 'not_found'
    }

def search_papers_by_keyword(keyword, num_results=10):
    """Search for papers by keyword, returns metadata list"""
    # Use CrossRef API for search, only return metadata, no Sci-Hub query
    papers = []
    try:
        url = f"https://api.crossref.org/works?query={keyword}&rows={num_results}"
        response = requests.get(url, timeout=90)
        if response.status_code == 200:
            data = response.json()
            for item in data['message']['items']:
                paper_info = {
                    'title': item.get('title', [''])[0] if item.get('title') else '',
                    'author': ', '.join([author.get('given', '') + ' ' + author.get('family', '') 
                                       for author in item.get('author', [])]),
                    'year': item.get('published-print', {}).get('date-parts', [[]])[0][0] if item.get('published-print') else '',
                    'doi': item.get('DOI', ''),
                    'status': 'metadata_only',  # Indicate this is metadata only
                    'note': 'Use search_scihub_by_doi to get PDF URL'
                }
                papers.append(paper_info)
    except Exception as e:
        print(f"Search error: {str(e)}")
    
    return papers

def download_paper(pdf_url, output_path):
    """Download paper PDF"""
    sh = SciHub()
    try:
        sh.download(pdf_url, output_path)
        return True
    except Exception as e:
        print(f"Download error: {str(e)}")
        return False


if __name__ == "__main__":
    print("Sci-Hub Paper Search Test\n")

    # 1. DOI search test
    print("1. Search paper by DOI")
    test_doi = "10.1002/jcad.12075"  # A neuroscience-related paper
    result = search_paper_by_doi(test_doi)
    
    if result['status'] == 'success':
        print(f"Title: {result['title']}")
        print(f"Author: {result['author']}")
        print(f"Year: {result['year']}")
        print(f"PDF URL: {result['pdf_url']}")
        
        # Try to download the paper
        output_file = f"paper_{test_doi.replace('/', '_')}.pdf"
        if download_paper(result['pdf_url'], output_file):
            print(f"Paper downloaded to: {output_file}")
        else:
            print("Paper download failed")
    else:
        print(f"Paper with DOI {test_doi} not found")

    # 2. Title search test
    print("\n2. Search paper by title")
    test_title = "Choosing Assessment Instruments for Posttraumatic Stress Disorder Screening and Outcome Research"
    result = search_paper_by_title(test_title)
    
    if result['status'] == 'success':
        print(f"DOI: {result['doi']}")
        print(f"Author: {result['author']}")
        print(f"Year: {result['year']}")
        print(f"PDF URL: {result['pdf_url']}")
    else:
        print(f"Paper with title '{test_title}' not found")

    # 3. Keyword search test
    print("\n3. Search papers by keyword")
    test_keyword = "artificial intelligence medicine 2023"
    papers = search_papers_by_keyword(test_keyword, num_results=3)
    
    for i, paper in enumerate(papers, 1):
        print(f"\nPaper {i}:")
        print(f"Title: {paper['title']}")
        print(f"DOI: {paper['doi']}")
        print(f"Author: {paper['author']}")
        print(f"Year: {paper['year']}")
        if paper.get('pdf_url'):
            print(f"PDF URL: {paper['pdf_url']}")

