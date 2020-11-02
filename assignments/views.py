from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Assignment, UploadedAssignment
from django.shortcuts import get_object_or_404
import PyPDF2

from .forms import AssignmentUploadForm
import docx
from django.views.generic.edit import FormView


def extract_pdf(filename):
    pdf_file = open('media/'+filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    text = ''
    for i in range(0, pdfReader.numPages):
        pdfObject = pdfReader.getPage(i)
        text += pdfObject.extractText()
    return text


def extract_docx(filename):
    doc = docx.Document('media/'+filename)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text)



class AssignmentListView(ListView):
    model = Assignment
    context_object_name = 'assignment_list'
    template_name = 'assignments/assignment_list.html'


# def assignment_submit(request, pk):
#     assignment = get_object_or_404(Assignment, pk=pk)
#     if request.method == 'POST':
#         # form is sent
#         form = AssignmentUploadForm(data=request.POST)
#         if form.is_valid():
#             pass
#             # # form data is valid
#             # cd = form.cleaned_data
#             # new_item = form.save(commit=False)
#             #
#             # # assign current user to the item
#             # new_item.user = request.user
#             # new_item.save()
#             # create_action(request.user, 'bookmarked image', new_item)
#             # messages.success(request, 'Image added successfully')
#             #
#             # # redirect to new created item detail view
#             # return redirect(new_item.get_absolute_url())
#     else:
#         # build form with data provided by the bookmarklet via GET
#         form = AssignmentUploadForm(data=request.GET)
#     return render(request, 'assignments/assignment_detail.html', {'assignment':assignment, 'form':form})

# class AssignmentDetailView(DetailView, FormView):
#     model = Assignment
#     context_object_name = 'assignment'
#     form_class = AssignmentUploadForm
#     success_url = '/assignments'
#     template_name = 'assignments/assignment_detail.html'
#
#     def form_valid(self, form):
#         form.save()
#         return super(AssignmentDetailView, self).form_valid(form)


def assignmentdetailview(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    # text = ''

    if request.method != 'POST':
        form = AssignmentUploadForm(request.GET)
    else:
        # POST data submitted; process data.
        form = AssignmentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.assignment = assignment
            new_entry.student = request.user
            new_entry.save()
            print("uploaded file")
            # text = extract_pdf(new_entry.upload_file)
            # text

            # return render(request, 'assignments/submitted_list.html')
            # return redirect(reverse('u', kwargs={'uuid': self.fcc_form.uuid}))
            return redirect(reverse('uploaded_detail', args=[str(new_entry.id)]))
    context = {'assignment': assignment, 'form': form,}
    return render(request, 'assignments/assignment_detail.html', context)


def submittedassignment(request):
    submitted_list = UploadedAssignment.objects.filter(student=request.user)
    return render(request, 'assignments/submitted_list.html', {'submitted_list':submitted_list})


# class UploadedDetailView(DetailView):
#     model = UploadedAssignment
#     context_object_name = 'uploaded'
#     template_name = 'assignments/uploaded_detail.html'

def UploadedDetailView(request, pk):
    uploaded = get_object_or_404(UploadedAssignment, pk=pk)
    if str(uploaded.upload_file).endswith('pdf'):
        text = extract_pdf(str(uploaded.upload_file))
    else:
        text = extract_docx(str(uploaded.upload_file))
    return render(request, 'assignments/uploaded_detail.html', {'uploaded':uploaded, 'text':text})

















