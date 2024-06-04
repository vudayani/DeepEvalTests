import pytest
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase


def test_case():
    answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5, model="gpt-3.5-turbo", include_reason=True)
    test_case = LLMTestCase(
        input="JPA functionality",
        # Replace this with the actual output from your LLM application
        actual_output="""
Generated using the description: JPA functionality with an integration test. Include all Java code in the same package.

To add the Spring Data JPA functionality with an integration test to an existing Maven project, follow these steps:

### Step 1: Add Dependencies
Add the following dependencies to your `pom.xml` file for Spring Data JPA and testing:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

### Step 2: Create Entity Class
Create a `Person` entity class with properties `name` and `phoneNumber` in the package `org.springframework.samples.petclinic.ai.jpa`:

```java
package org.springframework.samples.petclinic.ai.jpa;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Person {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private String phoneNumber;

    // Constructors, getters, and setters
}
```

### Step 3: Create Repository Interface
Create a `PersonRepository` interface in the same package to interact with the database:

```java
package org.springframework.samples.petclinic.ai.jpa;

import org.springframework.data.jpa.repository.JpaRepository;

public interface PersonRepository extends JpaRepository<Person, Long> {
}
```

### Step 4: Create Service Class
Create a `PersonService` class in the same package to handle business logic:

```java
package org.springframework.samples.petclinic.ai.jpa;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class PersonService {

    @Autowired
    private PersonRepository personRepository;

    // Service methods
}
```

### Step 5: Create Controller Class
Create a `PersonController` class in the same package to handle HTTP requests:

```java
package org.springframework.samples.petclinic.ai.jpa;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PersonController {

    @Autowired
    private PersonService personService;

    // Controller methods
}
```

### Step 6: Integration Test
Create an integration test class in the same package to test interactions between layers:

```java
package org.springframework.samples.petclinic.ai.jpa;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.web.server.LocalServerPort;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class PersonIntegrationTest {

    @LocalServerPort
    private int port;

    @Autowired
    private TestRestTemplate restTemplate;

    @Test
    public void testIntegration() {
        // Integration test logic
    }
}
```

### Step 7: Application Properties
Add the necessary configurations to your `application.properties` file with the appropriate database settings. Set the `info` field to `properties` for this section.

```properties
# Database configuration
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
```

By following these steps, you can integrate Spring Data JPA functionality with an integration test into your existing Maven project. 

### Tutorials for Learning More:
1. [Spring Data JPA - Official Documentation](https://spring.io/projects/spring-data-jpa)
2. [Baeldung - Introduction to Spring Data JPA](https://www.baeldung.com/spring-data-jpa)
3. [Spring Data JPA Tutorial](https://www.javatpoint.com/spring-data-jpa-tutorial)
4. [Spring Data JPA with Hibernate - Tutorial](https://www.callicoder.com/spring-boot-spring-data-jpa-hibernate-example/)
5. [Spring Data JPA - Tutorialspoint](https://www.tutorialspoint.com/spring_data/spring_data_jpa.htm)
        """,
        retrieval_context=[
            """This is the system chat message. Your task is to create Java source test code for an application that performs the following actions:

1. Create a Java source test code application using Spring Boot framework version 3.0. Do not use Spring Initializr.

Use the following project information for the solution:

Main Spring project: [Spring Project Name]
Package name: [Package Name]
Build tool: [Build Tool]
Spring boot version: [Spring Boot Version]
Java version: [Java Version]
User prompt: [Description]

Ensure that your solution meets the following criteria:

1. Provide steps for adding code to an existing project, rather than creating a new project.
2. Include build tool dependency management configuration for the project (partial file, not full project dependency configuration).
3. The spring-boot-starter-test is the primary dependency that contains the majority of elements required for our tests.
3. Utilize the Maven artifactId "spring-boot-starter-test" as a dependency for JUnit-related functionality, avoiding the direct addition of a JUnit dependency.
4. Place the test code under /src/test/java/ in appropriate package. Use the Package name as the root package and place the files in sub-packages accordingly.
5. Include unit tests for each architectural layer (Controller, Service, Repository) as appropriate.
6. Include an integration test if there are multiple architectural layers.
7. In the test class, import all the necessary packages and annotations.
8. Use @SpringBootTest annotation to load the Spring application context for integration tests. Use @WebMvcTest annotation to load only the web layer for unit tests.
8. Use the @InjectMocks annotation to automatically inject the CabController instance into the test class. Use the @Mock annotation to create a mock instance.
9. Write test methods to cover different scenarios. In the test method, set up the necessary mock behavior using when and thenReturn methods from Mockito.
10. Use assertion methods from JUnit to verify the expected results.
11. Ensure the sample code resembles that available in the GitHub repositories of the organization located at https://github.com/spring-guides/gs-testing-web.git.
12. When generating markdown for code blocks in the final response, include an appropriate value for the "info" field."""
        ],
    )
    assert_test(test_case, [answer_relevancy_metric])
