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
- **.NET 9**: Latest LTS version with enhanced performance and new features
- **Blazor**: Framework for building interactive client-side and server-side web UI with C#
- **ASP.NET Core**: Mature web framework for building web apps and APIs
- **Entity Framework Core**: ORM for .NET with LINQ support
- **MAUI**: .NET Multi-platform App UI for cross-platform development
- **MediatR**: Implementation of mediator pattern for in-process messaging
- **Minimal APIs**: Lightweight approach for building HTTP APIs in ASP.NET Core
- **Minimal API Auth**: Authentication for Minimal APIs
- **Serilog**: Structured logging library with rich configuration options
- **Polly**: Resilience and transient-fault-handling library
- **Dapper**: Lightweight ORM focusing on performance
- **gRPC**: High-performance RPC framework for distributed systems

### Trial
- **.NET 8**: Previous LTS version with strong ecosystem support
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
- **Angular 19**: Latest version with improved performance and features
- **Angular Signals**: Core reactive primitive for state management
- **Angular Standalone Components**: Components without NgModule
- **Angular Material**: UI component library using Material Design
- **RxJS**: Reactive programming library for JavaScript
- **NgRx**: Reactive state management with Redux pattern
- **Angular CLI**: Command-line interface for Angular
- **Angular Universal**: Server-side rendering (SSR) for Angular
- **TypeScript**: Typed superset of JavaScript
- **Jest**: Testing framework for JavaScript
- **Cypress**: End-to-end testing framework
- **Playwright**: End-to-end testing framework
- **Tailwind CSS**: Utility-first CSS framework

### Trial
- **Angular Server Components**: Server-side rendering with hydration
- **Nx**: Extensible dev tools for monorepos
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
- **Angular DSL**: Domain-specific language support
- **Taiga UI**: UI kit with unique visual style
- **Angular Three**: 3D graphics in Angular
- **Angular Testing Library**: Testing utilities for Angular
- **Web Components Interop**: Improved custom elements integration

### Hold
- **AngularJS**: Legacy version of Angular (1.x)
- **Angular 16 and older**: Previous versions of Angular
- **Protractor**: E2E testing (replaced by Cypress/Playwright)
- **ngx-bootstrap**: Use Angular Material or PrimeNG instead
- **Template-driven forms**: Reactive forms preferred in most cases
- **jQuery with Angular**: Avoid mixing Angular with jQuery
- **Clarity Design**: Reduced momentum compared to alternatives
- **Angular HTTP (in favor of HttpClient)**: Older HTTP implementation
- **Karma**: Test runner replaced by Jest
- **Jasmine**: Testing framework replaced by Jest

---

## Testing Frameworks and Libraries

### Adopt
- **Playwright**: Browser automation and end-to-end testing
- **Jest**: JavaScript testing framework
- **xUnit.net**: Unit testing framework for .NET
- **NUnit**: Unit testing framework for .NET
- **Moq**: Mocking framework for .NET
- **Cypress**: End-to-end testing framework
- **Pytest**: Testing framework for Python
- **FluentAssertions**: Fluent assertions for .NET
- **Testing Library**: DOM testing utilities
- **TestContainers**: Integration testing with containerized dependencies

### Trial
- **Vitest**: Vite-native testing framework
- **Selenium 4**: Browser automation library
- **BDDfy**: BDD testing framework for .NET
- **Robot Framework**: Generic test automation framework
- **Hypothesis**: Property-based testing for Python
- **Mock Service Worker**: API mocking for browser and Node
- **Specflow**: BDD framework for .NET
- **NSubstitute**: Mocking framework for .NET

### Assess
- **k6**: Performance testing tool
- **WebdriverIO**: Next-gen browser and mobile testing
- **Snapshottest**: Snapshot testing for Python
- **Stryker Mutator**: Mutation testing
- **AI-assisted Testing**: AI-driven test generation and maintenance
- **Pytest-BDD**: BDD framework for pytest
- **Appium 2**: Mobile app testing framework
- **Test Impact Analysis**: Tools for intelligent test selection

### Hold
- **Jasmine**: JavaScript testing framework (replaced by Jest)
- **MSTest** (legacy version): Older Microsoft testing framework
- **unittest** (Python standard library): Basic testing in Python
- **QUnit**: Older JavaScript testing library
- **Karma**: Test runner for JavaScript (replaced by Jest)
- **Protractor**: E2E testing framework (replaced by Cypress/Playwright)
- **Nightwatch.js**: E2E testing with reduced adoption
- **Behave**: Python BDD framework with less momentum
