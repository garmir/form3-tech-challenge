import re
import requests
import logging

def detect_ssrf(url):
    """
    Detects SSRF vulnerabilities in a URL.

    Args:
        url (str): The URL to check for SSRF vulnerabilities.

    Returns:
        bool: True if the URL contains an SSRF vulnerability, False otherwise.
    """
    # Define the regular expression pattern to match legitimate AWS instance URLs
    aws_url_pattern = r'https?://([a-zA-Z0-9-]+\.)?(s3|ec2|elasticbeanstalk|lambda)\.amazonaws\.com/.*'

    # Check if the URL matches the AWS instance URL pattern
    if re.match(aws_url_pattern, url):
        logging.warning(f"SSRF detected for URL: {url}")
        
        # Send the detected SSRF URL to alerting API (e.g. Crowdstrike)
        try:
            response = requests.post('https://api.crowdstrike.com/ssrf_alerts', json={'url': url})
            if response.status_code != 200:
                logging.error(f"Failed to send SSRF URL to CrowdStrike API: {response.content}")
        except Exception as e:
            logging.error(f"Failed to send SSRF URL to CrowdStrike API: {str(e)}")
        
        return True
    else:
        return False
