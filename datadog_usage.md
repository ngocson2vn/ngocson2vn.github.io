##### Table of Contents  
[I. Basic Usage](#basic_usage)  
&nbsp;&nbsp;[1. Datadog-AWS Integration](#basic_integration)  
&nbsp;&nbsp;[2. The Datadog Agent](#basic_agent)  
&nbsp;&nbsp;[3. Check Infrastructure](#basic_infra)  
&nbsp;&nbsp;[4. How to get Metrics](#basic_metrics)  
&nbsp;&nbsp;[5. How to make Graph and Dashboard](#basic_graph)  
&nbsp;&nbsp;[6. Monitoring](#basic_monitoring)  

[II. Advanced Usage](#advanced_usage)  
&nbsp;&nbsp;[1. Send custom metrics to Datadog](#advanced_metrics)  

<a name="basic_usage"/>
# I. Basic Usage

<a name="basic_integration"/>
## 1. Datadog-AWS Integration
The details are described in this page  
http://docs.datadoghq.com/integrations/aws/  

* After the integration process is finished, click on the **Integrations** tab to see the installed services:  
<img src="http://ngocson2vn.github.io/datadog/integrated.png" alt="installed services">  

<a name="basic_agent"/>
## 2. The Datadog Agent
* Getting Started with the Agent  
http://docs.datadoghq.com/guides/basic_agent_usage/

* Installation  
From the left sidebar, select **Integrations**, then select **Agent**, and select your platform. The installation instruction will be shown. You should follow this instruction to install the Datadog Agent on your EC2 instances.  
<img src="http://ngocson2vn.github.io/datadog/agent.png" alt="Agent Installation">

* Starting and Stopping the Agent  
To manually start the Agent:  
`sudo /etc/init.d/datadog-agent start`  
<br>
To stop the Agent:  
`sudo /etc/init.d/datadog-agent stop`  
<br>
To restart the Agent and to reload the configuration files:  
`sudo /etc/init.d/datadog-agent restart`  

* Status and Information  
To check if the Agent is running: (since 3.8.0)  
`sudo /etc/init.d/datadog-agent status`  
<br>
To receive information about the Agent’s state:  
`sudo /etc/init.d/datadog-agent info`  
<br>
Tracebacks for errors can be retrieved by setting the -v flag: (since 3.8.0)  
`sudo /etc/init.d/datadog-agent info -v`  

* For more information  
http://docs.datadoghq.com/guides/basic_agent_usage/  
http://docs.datadoghq.com/guides/dogstatsd/

<a name="basic_infra"/>
## 3. Check Infrastructure
* From the left sidebar, select **Infrastructure > Infrastructure List**. You will see a list of EC2 instances belonging to your EC2 service.  
<img src="http://ngocson2vn.github.io/datadog/infrastructure.png" alt="Infrastructure List">

<a name="basic_metrics"/>
## 4. How to get Metrics
* For each installed service, there are corresponding metrics. For example, click on **Amazon EC2**, select **Metrics** tab, metrics list will be shown:  
<img src="http://ngocson2vn.github.io/datadog/metrics_ec2.png" alt="EC2 metrics">

* The first place you can check for metrics is the Metrics Explorer.
<img src="http://ngocson2vn.github.io/datadog/metrics_explorer.png" alt="Metrics Explorer">  
<br>
For example, check metric `aws.ec2.cpuutilization`  
<img src="http://ngocson2vn.github.io/datadog/metrics_explorer_sample01.png" alt="Metrics Explorer Sample">  

<a name="basic_graph"/>
## 5. How to make Graph and Dashboard
The following steps will guide you to make Graph and Dashboard  

* Choose the Metric to graph  
Start with the Metrics Explorer and input what metrics you want to make graph into `Graph:` textbox. For example, we want to make graph for metric `aws.ec2.cpuutilization.maximum`:  
<img src="http://ngocson2vn.github.io/datadog/graph_dashboard01.png" alt="Graph and Dashboard">  

* Save this graph to a new dashboard:  
<img src="http://ngocson2vn.github.io/datadog/graph_dashboard02.png" alt="Graph and Dashboard">  

* Open dashboard  
From the left sidebar, select **Dashboards> Dashboard List**:  
<img src="http://ngocson2vn.github.io/datadog/graph_dashboard03.png" alt="Graph and Dashboard">  
<br>
Click on dashboard name **My AWS EC2**
<img src="http://ngocson2vn.github.io/datadog/graph_dashboard04.png" alt="Graph and Dashboard"> 

* For more information  
 http://docs.datadoghq.com/graphing/
http://docs.datadoghq.com/ja/graphing/

<a name="basic_monitoring" />
## 6. Monitoring
* Monitor type: from the left sidebar, select **Monitors > New Monitor**. The list of monitor types will be shown  
<img src="http://ngocson2vn.github.io/datadog/monitor_type.png" alt="Monitor type">  

* Creating Host Monitors  
From the list of monitor types, select **Host**. Configure it as follows:  
<img src="http://ngocson2vn.github.io/datadog/monitor_host.png" alt="Monitor Host">  
<br>
Next, in order to confirm alert, we stop the Datadog Agent on a host  
`sudo /etc/init.d/datadog-agent stop`  
<br>
Wait for 2 minutes, then check **Triggered Monitors**
<img src="http://ngocson2vn.github.io/datadog/triggered.png" alt="Triggered Monitors">  
<br>
Click on alert name, it should show  
<img src="http://ngocson2vn.github.io/datadog/alert_status.png" alt="Triggered Monitors">  
<br>
Check email  
<br>
<img src="http://ngocson2vn.github.io/datadog/alert_mail01.png" alt="Mail Alert">  
<br>
Wait for 10 minutes, then check email again  
<br>
<img src="http://ngocson2vn.github.io/datadog/alert_mail02.png" alt="Mail Alert">  
<br>
In order to check recovery, we start the Datadog Agent again.  
`sudo /etc/init.d/datadog-agent start`  
<br>
Then, wait for a while, we will receive recovery email as follows  
<br>
<img src="http://ngocson2vn.github.io/datadog/recovered.png" alt="Mail Recovery">  

* For more information
http://docs.datadoghq.com/guides/monitoring/  
http://docs.datadoghq.com/ja/guides/monitoring/  

<a name="advanced_usage" />
# II. Advanced Usage
<a name="advanced_metrics">
## 1. Send custom metrics to Datadog
