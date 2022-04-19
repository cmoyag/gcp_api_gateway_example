Exportar requeriment

pip freeze > requirements.txt

Tutorial paso a paso

1 Crear imagen
docker build --tag apiv1:dev .

DEPLOY

# Set an environment variable with your GCP Project ID
export GOOGLE_CLOUD_PROJECT=<PROJECT_ID>

# Submit a build using Google Cloud Build
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/apiv1

# Deploy to Cloud Run
gcloud run deploy helloworld \
--image gcr.io/${GOOGLE_CLOUD_PROJECT}/apiv1

GCP

Crear Imagen

gcloud builds submit --tag us-central1-docker.pkg.dev/softlution-1342/cloudrun/apiv1:dev
