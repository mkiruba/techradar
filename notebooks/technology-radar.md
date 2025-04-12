# Technology Radar
## Frameworks, Libraries, and Testing Tools for .NET and Angular

### Introduction

This Technology Radar provides an opinionated guide to technology frontiers that have significant impact on software development. The Radar captures the output of discussions and experiences with these technologies in the industry.

Our Technology Radar is divided into four quadrants:
- **Adopt**: Technologies we have high confidence in to serve our purpose
- **Trial**: Technologies worth pursuing; understand how they might impact your development 
- **Assess**: Technologies worth exploring to understand how they might affect your projects
- **Hold**: Technologies that should be approached with caution

Each technology is represented as a blip on the radar.

---

## .NET Ecosystem

### Adopt
- **.NET 8**: Latest LTS version with performance improvements and new features
- **ASP.NET Core**: Mature web framework for building web apps and APIs
- **Entity Framework Core**: ORM for .NET with LINQ support
- **Blazor**: Framework for building interactive client-side web UI with C#
- **MediatR**: Implementation of mediator pattern for in-process messaging
- **AutoMapper**: Object-to-object mapping library
- **Serilog**: Structured logging library with rich configuration options
- **Polly**: Resilience and transient-fault-handling library
- **Dapper**: Lightweight ORM focusing on performance
- **Minimal APIs**: Lightweight approach for building HTTP APIs in ASP.NET Core
- **gRPC**: High-performance RPC framework for distributed systems

### Trial
- **MAUI**: .NET Multi-platform App UI for cross-platform development
- **Hot Chocolate**: GraphQL server for .NET
- **MassTransit**: Distributed application framework for message-based architecture
- **IdentityServer**: OpenID Connect and OAuth 2.0 framework
- **Refit**: Automatic type-safe REST library for .NET
- **YARP**: Reverse proxy toolkit for building fast proxy servers
- **Bogus**: Fake data generator
- **SignalR**: Library for real-time web functionality
- **Spectre.Console**: Beautiful console applications

### Assess
- **Orleans**: Framework for building distributed applications
- **Dapr**: Portable, event-driven runtime for distributed applications
- **ML.NET**: Machine learning framework for .NET
- **FASTER**: Fast key-value store with larger-than-memory data
- **Duende IdentityServer**: Commercial version of IdentityServer
- **Carter**: Library to help achieve minimal APIs
- **Akka.NET**: Actor model implementation for .NET
- **NodaTime**: Better date and time handling

### Hold
- **.NET Framework** (in favor of .NET Core/.NET 5+): Legacy framework
- **WebForms**: Legacy web development framework
- **WCF**: Legacy service framework (consider gRPC or REST instead)
- **Nancy**: Lightweight HTTP framework (reduced activity)
- **Unity Container**: IoC container with reduced community support
- **NHibernate**: Older ORM that has been largely replaced by EF Core

---

## Angular Ecosystem

### Adopt
- **Angular 17**: Latest version with improved performance and features
- **Angular Material**: UI component library using Material Design
- **RxJS**: Reactive programming library for JavaScript
- **NgRx**: Reactive state management with Redux pattern
- **Angular CLI**: Command-line interface for Angular
- **Angular Universal**: Server-side rendering (SSR) for Angular
- **TypeScript**: Typed superset of JavaScript
- **Jest**: Testing framework for JavaScript
- **Cypress**: End-to-end testing framework
- **Tailwind CSS**: Utility-first CSS framework
- **Angular Signals**: New reactive primitive for state management

### Trial
- **Nx**: Extensible dev tools for monorepos
- **Angular Standalone Components**: Components without NgModule
- **Storybook**: UI component development environment
- **PrimeNG**: Rich UI component library for Angular
- **Angular ESLint**: Linting utility for Angular projects
- **Transloco**: Internationalization library
- **NgOptimizedImage**: Image optimization directives
- **Angular CDK**: Component Dev Kit without visual styling
- **NgRx Component Store**: Standalone state management

### Assess
- **Angular Elements**: Package Angular components as custom elements
- **Angular Ionic**: UI framework for mobile development
- **Akita**: State management with minimal boilerplate
- **Angular Hydration**: Improved client-side hydration
- **Taiga UI**: UI kit with unique visual style
- **Angular Three**: 3D graphics in Angular
- **Angular Testing Library**: Testing utilities for Angular
- **Angular PWA**: Progressive Web App features

### Hold
- **AngularJS**: Legacy version of Angular (1.x)
- **Protractor**: E2E testing (being replaced by Cypress/Playwright)
- **ngx-bootstrap**: Use Angular Material or PrimeNG instead
- **Template-driven forms**: Reactive forms preferred in most cases
- **jQuery with Angular**: Avoid mixing Angular with jQuery
- **Clarity Design**: Reduced momentum compared to alternatives
- **Angular HTTP (in favor of HttpClient)**: Older HTTP implementation
- **Karma**: Test runner being replaced by Jest

---

## Testing Frameworks and Libraries

### Adopt
- **xUnit.net**: Unit testing framework for .NET
- **NUnit**: Unit testing framework for .NET
- **Moq**: Mocking framework for .NET
- **Pytest**: Testing framework for Python
- **Jasmine**: Testing framework for JavaScript
- **Jest**: JavaScript testing framework
- **Cypress**: End-to-end testing framework
- **Playwright**: Browser automation and testing

### Trial
- **FluentAssertions**: Fluent assertions for .NET
- **Selenium 4**: Browser automation library
- **TestContainers**: Integration testing with containerized dependencies
- **BDDfy**: BDD testing framework for .NET
- **Robot Framework**: Generic test automation framework
- **Hypothesis**: Property-based testing for Python
- **Mock Service Worker**: API mocking for browser and Node
- **Testing Library**: DOM testing utilities

### Assess
- **Specflow**: BDD framework for .NET
- **NSubstitute**: Mocking framework for .NET
- **Snapshottest**: Snapshot testing for Python
- **Stryker Mutator**: Mutation testing
- **k6**: Performance testing tool
- **WebdriverIO**: Next-gen browser and mobile testing
- **Vitest**: Vite-native testing framework
- **Pytest-BDD**: BDD framework for pytest

### Hold
- **MSTest** (legacy version): Older Microsoft testing framework
- **unittest** (Python standard library): Basic testing in Python
- **QUnit**: Older JavaScript testing library
- **Karma** (being replaced): Test runner for JavaScript
- **Jasmine** (being replaced by Jest): JavaScript testing framework
- **Protractor**: Being phased out for E2E testing
- **Nightwatch.js**: E2E testing with reduced adoption
- **Behave**: Python BDD framework with less momentum

---

## Performance & Monitoring Tools

### Adopt
- **Application Insights**: App monitoring solution for Azure
- **Prometheus**: Monitoring system with time-series database
- **Grafana**: Observability platform
- **Elastic APM**: Application performance monitoring
- **New Relic**: Cloud-based observability platform
- **Datadog**: Monitoring and security platform
- **Sentry**: Error tracking and performance monitoring
- **Jaeger**: Distributed tracing system

### Trial
- **OpenTelemetry**: Observability framework
- **Dynatrace**: AI-powered observability platform
- **BenchmarkDotNet**: Benchmarking for .NET
- **Pyinstrument**: Python profiler
- **Honeycomb**: Observability for distributed systems
- **cProfile**: Python profiling library
- **Lighthouse**: Web performance analysis tool
- **SigNoz**: Open-source APM alternative

### Assess
- **MiniProfiler**: Simple profiler for .NET and Ruby
- **AppMetrics**: .NET application metrics
- **Locust**: Performance testing tool
- **Skywalking**: APM, tracing and service mesh
- **py-spy**: Sampling profiler for Python
- **FlameGraph**: Stack trace visualization
- **Aspecto**: Microservices observability
- **Speedscope**: Interactive flamegraph explorer

### Hold
- **Log4Net**: Logging library for .NET
- **NLog**: Logging platform for .NET (Serilog preferred)
- **Logstash**: Log processing pipeline (complex setup)
- **StatsD**: Simple statistics aggregation
- **AppDynamics**: APM solution (high cost)
- **Performance Counter**: Windows legacy metrics
- **PerfMon**: Windows Performance Monitor
- **Splunk**: Log monitoring (cost concerns)

---

## DevOps & CI/CD

### Adopt
- **GitHub Actions**: CI/CD and automation platform
- **Azure DevOps**: DevOps service platform
- **Docker**: Containerization platform
- **Kubernetes**: Container orchestration
- **Terraform**: Infrastructure as code
- **Helm**: Kubernetes package manager
- **ArgoCD**: GitOps continuous delivery
- **SonarQube**: Code quality platform

### Trial
- **Pulumi**: Infrastructure as code using programming languages
- **GitHub Copilot**: AI pair programmer
- **Buildkite**: CI/CD platform
- **Octopus Deploy**: Deployment automation server
- **GitLab CI**: CI/CD in GitLab
- **Azure Bicep**: Domain-specific language for ARM templates
- **Flux CD**: GitOps for Kubernetes
- **Tekton**: Kubernetes-native CI/CD

### Assess
- **Dapr**: Distributed application runtime
- **Crossplane**: Kubernetes add-on for cloud resources
- **Kustomize**: Kubernetes configuration customization
- **Cilium**: Networking, security, and observability
- **Ansible**: Automation platform
- **Skaffold**: Kubernetes development workflow
- **Backstage**: Developer portal platform
- **OpenCost**: Kubernetes cost monitoring

### Hold
- **Jenkins**: CI/CD server (maintenance overhead)
- **TeamCity**: CI/CD server (cost and alternatives)
- **Chef**: Configuration management (complexity)
- **Puppet**: Configuration management (alternatives preferred)
- **CircleCI**: CI/CD platform (cost concerns)
- **Travis CI**: CI/CD service (reduced free tier)
- **Docker Swarm**: Container orchestration (K8s dominance)
- **Mesos**: Distributed systems kernel (declining use)
