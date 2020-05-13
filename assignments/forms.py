from .models import UploadedAssignment
from django import forms


class AssignmentUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedAssignment
        fields = ['upload_file', ]

    # def clean_upload_file(self):
    #     upload_file = self.cleaned_data.get('upload_file')
    #     filename = str(upload_file)
    #     valid_extensions = ['pdf', 'docx']
    #     extension = filename.rsplit('.', 1)[1].lower()
    #     print(extension)
    #     if extension not in valid_extensions:
    #         raise forms.ValidationError('The given file does not ' \
    #                                     'match valid extensions.')
    #     return upload_file

