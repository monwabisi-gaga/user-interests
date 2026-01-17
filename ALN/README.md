aln: A Creator's Hub
Project Overview
The "aln" is a microservices-based platform for musicians, photographers, and cinematographers to share, collaborate, and monetize their work. The platform aims to showcase unique African talent with a distinct "aln-style" front-end aesthetic.

The platform will be deployed on a bare-metal Kubernetes cluster, ensuring scalability, resilience, and full control over the infrastructure.

Core Architectural Components
The system is designed as a series of independent microservices that communicate with each other. This approach allows for greater flexibility, scalability, and ease of maintenance.

Ingestion Service: Handles the initial upload of content.

Transcoding Service: Processes raw content (video, audio, images) into standardized, low-bitrate formats.

Storage Service: Stores both raw and processed assets.

Content Management Service: Manages all content metadata.

User/Dashboard Service: The front-end for creators to upload and manage their content.

Streaming/Viewing Service: Delivers content to end-users.

Analytics Service: Gathers and visualizes metrics like views and geotagging.

Payment/Collaboration Service: Manages the paygate and revenue sharing.

API Gateway: A single entry point for all API requests.

Technology Stack
Orchestration: Kubernetes

Containerization: Docker

Transcoding: FFmpeg

Object Storage: MinIO (S3-compatible)

Message Queue: RabbitMQ

Back-end: Python (FastAPI)

Front-end: React / Vue.js

Analytics: Prometheus & Grafana

Task Breakdown: A Step-by-Step Roadmap
We will complete the project by tackling one task at a time. Each task builds upon the previous one.

Task 1: Ingestion Service & Transcoding Service
Status: Completed

We have successfully started the development of the first two services. The goal was to create a functional pipeline that accepts a file upload and triggers a transcoding process.

Ingestion Service

Built a REST API using FastAPI to handle file uploads.

Validated the uploaded file type.

Generated a unique content ID for the file.

Transcoding Service

Used FFmpeg to transcode videos to a standardized 1080p MP4 format.

Created a simple function to handle the transcoding process.

Task 2: Implementing a Message Queue and MinIO
Status: Completed

We've integrated a message queue and an object storage solution to create a robust and scalable architecture. The message queue decouples the services, ensuring they can operate independently, while object storage provides a central, accessible location for all our media assets.

Message Queue Integration (RabbitMQ)

The Ingestion Service was modified to act as a producer. It now publishes a message to a RabbitMQ queue after a successful file upload, containing the content_id and file details.

The Transcoding Service was converted into a consumer. It continuously listens for messages on the queue and initiates a transcoding job for each message it receives.

MinIO Integration

We set up MinIO as our self-hosted object storage solution.

The Ingestion Service now uploads raw files directly to a designated "raw-assets" bucket in MinIO.

The Transcoding Service downloads the raw file from MinIO, transcodes it, and then uploads the final, processed file to a separate "transcoded-assets" bucket.

Task 3: Content Management Service & Database
Status: To Do

This service will act as the source of truth for all content metadata.

Database Setup

Choose and set up a database (e.g., PostgreSQL, MongoDB).

Define a schema for content metadata (title, description, collaborators, status, etc.).

Content Management Service (CMS)

Create a FastAPI service to manage content metadata.

Develop endpoints for creating, reading, updating, and deleting content information.

The Ingestion Service will call the CMS to create an entry for the new content.

The Transcoding Service will call the CMS to update the content status to "processed" and add the location of the final file.