'''
Level 1 — Fundamentals
1. What is Docker?
2. Image vs Container
3. Docker Engine
4. Dockerfile
5. Build an image
6. Run a container
7. Port mapping
8. Container lifecycle
9. Docker logs
10. docker exec

Level 2 — Important Docker concepts
11. Volumes
12. Bind mounts
13. Environment variables
14. .dockerignore
15. Docker networks
16. Container-to-container communication
17. Docker image layers
18. Dockerfile best practices
19. CMD vs ENTRYPOINT
20. WORKDIR / COPY / RUN / ENV

You have already touched some of these through your practice folders.

Level 3 — Docker Compose
21. docker-compose.yml
22. Multiple services
23. Networks in Compose
24. Volumes in Compose
25. Environment variables
26. depends_on
27. Healthchecks
28. Restart policies
29. Development vs production configuration

Level 4 — Production Docker
This is especially important for MurphAI:

30. Multi-stage builds
31. Smaller images
32. Non-root users
33. Docker security
34. Health checks
35. Container logs
36. Resource limits
37. Secrets/configuration
38. Image tagging
39. Docker registry
40. Docker Hub / ECR

Level 5 — Real DevOps workflow
Eventually:

Code
 ↓
Dockerfile
 ↓
Docker Image
 ↓
GitHub Actions
 ↓
Build
 ↓
Test
 ↓
Push image
 ↓
AWS ECR
 ↓
Deploy
 ↓
Container running in AWS

That is where Docker becomes career-relevant, not just docker run nginx.
'''