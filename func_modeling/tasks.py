# Create your tasks here

from celery import shared_task
from .models import Function
from .modeling import build_plot
from PIL import Image
from django.conf import settings

@shared_task(name='graph maker')
def make_graph(id):
    function = Function.objects.get(pk=id)
    print(build_plot(id, function.function, function.interval, function.step))
    return build_plot(id, function.function, function.interval, function.step)


# def make_thumbnails(file_path, thumbnails=[]):
#     os.chdir(settings.IMAGES_DIR)
#     path, file = os.path.split(file_path)
#     file_name, ext = os.path.splitext(file)
#     zip_file = f"{file_name}.zip"
#     results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
#     try:
#         img = Image.open(file_path)
#         zipper = ZipFile(zip_file, 'w')
#         zipper.write(file)
#         os.remove(file_path)
#         for w, h in thumbnails:
#             img_copy = img.copy()
#             img_copy.thumbnail((w, h))
#             thumbnail_file = f'{file_name}_{w}x{h}.{ext}'
#             img_copy.save(thumbnail_file)
#             zipper.write(thumbnail_file)
#             os.remove(thumbnail_file)
#         img.close()
#         zipper.close()
#     except IOError as e:
#         print(e)
#     return results