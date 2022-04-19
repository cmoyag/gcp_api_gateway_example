Exportar requeriment

pip freeze > requirements.txt

Tutorial paso a paso
# Set an environment variable with your GCP Project ID
export GOOGLE_CLOUD_PROJECT=<PROJECT_ID>
# Crear imagen
docker build --tag apiv1:dev .
# Submit a build using Google Cloud Build
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/apiv1
# Deploy to Cloud Run
gcloud run deploy api-rest-v1 \
--image gcr.io/${GOOGLE_CLOUD_PROJECT}/apiv1


