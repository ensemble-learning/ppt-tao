---

@title[Introduction]
### Tao Cheng
### Research Assistant
### JCAP, Caltech

<span style="color:gray">Reaction mechanism of carbon dioxide reduction to propanol </span>

---

@title[Propanol is desired]
### Propanol is ideal production

<ol>
<li class="fragment"> 
The fuel efficiency of propanol approaches gasoline
    <ul>
    <li class="fragment">
    highest energy-mass density (30.93 kJ/g) of the C1-C3 alcohols
    </li>
    <li class="fragment">
    highest octane number (118) of the C1-C3 alcohols
    </li>
    </ul>
</li>

<!-- highest energy-mass density (30.93 kJ/g) of the C1-C3 alcohols -->
<!-- highest octane number (118) of the C1-C3 alcohols -->

<li class="fragment"> 
Propanol can be blended with gasoline to deliver a cleaner burning
</li>

<li class="fragment"> 
Propanol has high market value.
</li>

</ol>

+++

### Produce propanol from CO2RR

<ol>
<li class="fragment">
Current industrial production of propanol
    <ul>
    <li class="fragment">
    ethylene is hydroformylated to propionaldehyde using cobalt or rhodium-based catalysis
    </li>
    <li class="fragment">
    propionaldehyde is then reduced to propanol
    </li>
    </ul>
</li>

<li class="fragment">
electrochemical reduction of CO2 to propanol could be a cost-effective method
    <ul>
    <li class="fragment">
    3CO2 + 13H2O + 18e- = C3H7OH + 18OH- (E0 = 0.21 V)
    </li>
    </ul>
</li>

</ol>

---

### aws-gateway-executor

- A lightweight, fluent Java library
- For calling APIs on the Amazon Web Service API Gateway
- Inside any application running on the JVM
- Defines <span style="color:gray">AWSGateway</span>, <span style="color:gray">AWSTask</span> and <span style="color:gray">AWSResult</span>

+++

### AWSGateway

<span style="color:gray">A handle that represents an API on the AWS API Gateway.</span>

```Java
AWSGateway gateway = AWS.Gateway(echo-api-key)
                        .stage("beta")
                        .region(AWS.Region.OREGON)
                        .build();
```


+++

### AWSTask

<span style="color:gray">An executable object that represents an AWS Gateway call.</span>

```Java
AWSTask aTask = AWS.Task(gateway)
                   .resource("/echo")
                   .get();

```

+++

### AWSResult

<span style="color:gray">An object that represents the result of an AWS Gateway call.</span>

```Java
AWSResult aResult = aTask.execute();
```

---

@title[Batch Processing]
### SAMBA + Apache Spark Batch Processing

+++?gist=onetapbeyond/494e0fecaf0d6a2aa2acadfb8eb9d6e8&title=SAMBA Code-Walk
@[41-53](Build RDD[AWSTask])
@[57-62](Delegate RDD[AWSTask] to AWS Lambda)
@[64-75](Process RDD[AWSResult] from AWS Lambda)

---

#### SAMBA Deployment Architecture

@title[Deployment Architecture]
![SAMBA Deployment](https://onetapbeyond.github.io/resource/img/samba/new-samba-deploy.jpg)

---

#### Some Related Links

- [GitHub: SAMBA Package](https://github.com/onetapbeyond/lambda-spark-executor)
- [GitHub: SAMBA Examples](https://github.com/onetapbeyond/lambda-spark-executor#samba-examples)
- [GitHub: aws-gateway-executor](https://github.com/onetapbeyond/aws-gateway-executor)
- [GitHub: Apache Spark](https://github.com/apache/spark)
- [Apache Spark Packages](https://spark-packages.org/package/onetapbeyond/lambda-spark-executor)
