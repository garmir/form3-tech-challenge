# form3-tech-challenge
DB entry and detection rule for take home challenge

## Goal: 
Detecting Server Side Request Forgery (SSRF) attempts to unauthorized endpoints in a web application.

## Categorization: 
Execution / Command and Control

## Strategy Abstract: 
This alert is triggered when an HTTP request is made to an endpoint that is not authorized to be accessed by the web application. The rule is implemented by monitoring the HTTP traffic for requests containing user-controlled data in the URL or the body. The rule then checks whether the requested endpoint is authorized to be accessed by the application. If the requested endpoint is not authorized, an alert is generated.

## Technical Context: 
This alert uses the following technical data sources: web server logs, HTTP traffic, and application configuration files. The HTTP traffic is monitored using a network security device or an agent installed on the web server. The application configuration files specify the list of authorized endpoints that can be accessed by the web application. The alert can be implemented on various web application platforms such as ASP.NET, Java, and PHP.

## Blind Spots and Assumptions: 
This alert assumes that the application configuration files are properly configured to restrict access to unauthorized endpoints. Additionally, the alert may not detect SSRF attempts that bypass the web server and directly target internal resources.

## False Positives: 
- Legitimate requests to URLs that may appear suspicious but are actually authorized, such as requests made by security scanners or other authorized tools.
- Requests made to URLs that contain a domain name similar to the target AWS instance but are not actually related to it.
- Requests made to URLs that may appear to be an SSRF attempt, but are actually a result of misconfigured code or system components.

To address these potential false positives, the detection rule could be fine-tuned to include additional conditions or filters to help distinguish between legitimate and unauthorized requests. This could include whitelisting authorized IP addresses or user agents, filtering out requests made to known benign URLs, or using more advanced techniques such as machine learning or behavioural analysis to detect patterns of behaviour that are indicative of SSRF attacks.

## Validation:
To validate the rule, a testing scenario can be created by submitting an HTTP request with a user-controlled parameter targeting an unauthorized endpoint. The alert should fire and generate an alert in the SIEM.

## Priority: 
The severity or priority of the alert could be increased or decreased based on the results of any response actions taken. For example, if the response actions successfully prevent the attack from succeeding, the severity or priority of the alert could be decreased. Conversely, if the attack is successful or results in data loss or system downtime, the severity or priority of the alert could be increased.

## Response: 
For response actions, the severity or priority of the alert would depend on the nature of the alert and the impact it could have on the target system. For example, if the alert indicates that an unauthorized user is attempting to gain access to sensitive data, the priority would likely be high and immediate action would be required to prevent the attack from succeeding.

Some possible orchestration or automation actions that could be developed for response actions include:

- Blocking traffic from the source IP address or user agent associated with the unauthorized request.
- Alerting security personnel and initiating an investigation into the incident.
- Using an automation tool such as Ansible to automatically deploy security patches or configuration changes to prevent future attacks.
- Automatically creating a ticket in a helpdesk system to track the incident and ensure that it is addressed promptly.

## Additional Resources: 
(OWASP Top 10: Server Side Request Forgery (SSRF))[https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/] and NIST SP 800-115 Technical Guide to Information Security Testing and Assessment.
