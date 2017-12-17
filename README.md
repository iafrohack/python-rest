
# python-rest minimal design template

DISCLAIMER: This is an attempt to setup a highly decoupled
project in Python. As such, this can be found opinionated,
consume at your own risk (and pleasure...).

## Goal: Design a Python project that is highly scalable,
extensible, maintainable, testable and flexible while
encouraging fast development and productivity.

Project must also adhere to the Single Responsibility
Principle and enforce design patterns that conduce to
the overall project's goals.

## Tech Stack:

- Python3
- Eve Framework: http://python-eve.org/

## For a quick start:

1. Setup your Linux (Ubuntu) box as found on https://github.com/iafrohack/vagrant-django-setup
2. Then `pip install eve`
3. `pip install dependency_injector`
4. pip install python-interface

If you are on mac and followed step #1,
then all you have to do is access `192.168.50.4:5000` from your
browser on Mac.

eg: 192.168.50.4:5000/properties/12345

That's it!

Here is the Diagram of the project's structure:

![Alt Project Diagram](project-diagram.png?raw=true "Project Diagram")

# High-Level Details:

1. The request comes from the frontend client and hits our router.
Routers are in the routes directory. Each Resource has its own
router, so we we will have a properties router, and similarly, we
will have a users router when we are ready to handle user-related requests.
The routers' responsibility is to relay requests to the appropriate controllers,
and relay the controllers' response back to the client.

2. The controllers receive requests from the routers and control the flow
of getting the appropriate results. Controllers are also Resource-scoped, so each
resource will have its own controller, ie. PropertyController, UserController, etc...
Controllers do not handle any logic, they send requests to the appropriate services
and relay back the response to the routers.

3. Services are responsible for applying any business logic needed on requests
received from controllers, and relay back the response to the controllers.
Each Service is scoped to one and only one resource(very specific business logic).
For e.g the PropertyService is responsible for logic that is related to a property,
similarly a UserService is responsible for only user-related logic. The service knows
how to achieve all kinds of transformation and logic to handle a specific request
from the controller and return a response to it. If the service needs any data,
it sends those requests to the Data Repositories found in the Data Layer.

4. Data Repositories are responsible of only 1 task: Fetching and returning to the service
the requested data. It knows how to properly validate the request before retrieving it
from the data source.


With this structure, the separation of concerns is clearly enforced and the single responsibility
principle is observed: Each layer is responsible of one and only one task and knows how to do it
well. Each layer doesn't care about HOW the other layer achieves its tasks, it just knows
that it can achieve that particular task. It trusts the other layer to know how to do its job,
much like in a team we have to trust that each team member is very capable of achieving their
task at hand for the overall team objective.

Since each layer is completely separated from each other, we can test each layer in isolation,
and mock responses from the other layer, which makes our app a breeze to test.

# Implementation Details

## Interfaces Use

One noticeable detail is that we are using interfaces, even though interfaces are not
common in Python.

Interfaces are very powerful though and allow us to heavily decouple our app:

For example, if the PropertyService will need to get data from a Property Repository,
the service shouldn't care about any implementation details of the Property Repository:
It only cares that the repository adheres to a certain contract, and promises to get data
related to a certain property. So the service just cares that the Property Repository
implements a fetch_by_id method, it doesn't care HOW it implements it. As long as
the Property Repository instance that is passed to the Service PROVIDES the Property
Repository interface, the Property Service is fine with it, and can live with that.

Today our data source is MongoDb database, but tomorrow it can be a POSTGRESQL datasource.
This implementation detail is hidden from the Property Service, and it will be up to the
Property repository to handle this change.

We are using the Python interface package - https://pypi.python.org/pypi/python-interface/1.2.0 -
for its ease-of-use and support of our use of interfaces.

## Dependency Injection

Another Important Detail to notice in this project is that the instantiation of classes
is completely hidden from the various classes that have certain dependencies.

For instance, a Property Service requires an instance of an object that provides a Property
Repository interface when it is instantiated, but the Controller, which one might expect to handle the instantiation of the Property service, has no idea how the Property Service is instantiated.
The instantiation of a controller itself is delegated to a certain service that is specialized
in instantiating the controller. That service knows how to appropriately instantiate
a controller and 'inject' with it everything it needs to be created, including a
Property Service instance.

Instantiated classes have no knowledge of this service, they don't even know that it exists.

From the previous section, we declared:
"Today our data source is MongoDb database, but tomorrow it can be a POSTGRESQL datasource.":
our containers are handling the exact class that the Property Service is instantiated with.
Currently, the object that the PropertyService is instantiated with can be an instance of the PropertyRepositoryMongo that implements the PropertyRepository interface. In the future, if we
decide to use POSTGRESQL, then we can instead instantiate ('inject') the Property Service with
a PropertyRepositoryPostgre that also implements a PropertyRepository interface. All we have to do
at this point, is to make sure we run all of our unit-tests and ensure none broke. Then this is the
instance that will be used across the entire app: we don't have to chase over every place
we were using the old Mongo-based implementation, we simply turned a switch in our container...

This is Dependency Injection at its best...Such a powerful concept...

We are using the dependency_injector package found here https://pypi.python.org/pypi/dependency_injector .

All of our IOC containers are found in the `containers` directory.

You can read more about dependency injection on that link.

To quote from the page:

"Dependency injection is a software design pattern that implements Inversion of control for resolving dependencies. Formally, if object A depends on object B, object A must not create or import object B directly. Instead of this object A must provide a way for injecting object B. The responsibilities of objects creation and dependencies injection are delegated to external code - the dependency injector."

and:

"
Dependency injection pattern has few strict rules that should be followed:

1. The client delegates to the dependency injector the responsibility of injecting its dependencies - the service(s).
2. The client doesn’t know how to create the service, it knows only interface of the service. The service doesn’t know that it is used by the client.
3. The dependency injector knows how to create the client and the service, it also knows that the client depends on the service, and knows how to inject the service into the client.
4. The client and the service know nothing about the dependency injector.

"

and:

Dependency injection pattern provides the following advantages:

1. Control on application structure.
2. Decreased coupling between application components.
3. Increased code reusability.
4. Increased testability.
5. Increased maintainability.
6. Reconfiguration of system without rebuilding.

With the combination of the dependency injector and the fact that we are coding against
interfaces in this project, and the careful grounds-rules defined, we have packaged
a great piece of software that achieves all of the goals we had set ourselves.

Enjoy!
