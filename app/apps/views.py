from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Approval
from .forms import ApprovalForm
from .serializers import ApprovalSerializer

import pickle
import json
import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict, Counter
import keras.backend as K
import os



class ApprovalsView(viewsets.ModelViewSet):
	queryset = Approval.objects.all()
	serializer_class = ApprovalSerializer


def one_hot_encoded_value(df):
    path_to_file = os.path.dirname(os.path.abspath(__file__))
    columns_file = os.path.join(path_to_file, 'allcol.pkl')
    ohe_columns = joblib.load(columns_file)
    cat_columns=['Gender','Married','Education','Self_Employed','Property_Area']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    newdict={}
    for i in ohe_columns:
        if i in df_processed.columns:
            newdict[i] = df_processed[i].values
        else:
            newdict[i] = 0
    newdf = pd.DataFrame(newdict)
    return newdf


def confirm_loan_application(application):
    try:
        path_to_file = os.path.dirname(os.path.abspath(__file__))
        loans_file = os.path.join(path_to_file, 'loan_model.pkl')
        scalers_file = os.path.join(path_to_file, 'scalers.pkl')
        mdl = joblib.load(loans_file)
        scalers = joblib.load(scalers_file)
        X = scalers.transform(application)
        y_pred = mdl.predict(X)
        y_pred = (y_pred>0.56)
        newdf = pd.DataFrame(y_pred, columns=['Status'])
        newdf = newdf.replace({True: 'Loan Approved', False: 'Rejected: No creditworthiness'})
        K.clear_session()
        return (newdf.values[0][0],X[0])
    except ValueError as error:
        return (error.args[0])


def confirm_status_application(request):
	if request.method=='POST':
		form=ApprovalForm(request.POST)
		if form.is_valid():
			Firstname = form.cleaned_data['firstname']
			Lastname = form.cleaned_data['lastname']
			Dependents = form.cleaned_data['Dependents']
			ApplicantIncome = form.cleaned_data['ApplicantIncome']
			CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
			LoanAmount = form.cleaned_data['LoanAmount']
			Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
			Credit_History = form.cleaned_data['Credit_History']
			Gender = form.cleaned_data['Gender']
			Married = form.cleaned_data['Married']
			Education = form.cleaned_data['Education']
			Self_Employed = form.cleaned_data['Self_Employed']
			Property_Area = form.cleaned_data['Property_Area']
			request_dict = (request.POST).dict()
			df=pd.DataFrame(request_dict, index=[0])
			answer=confirm_loan_application(one_hot_encoded_value(df))[0]
			Xscalers=confirm_loan_application(one_hot_encoded_value(df))[1]
			if int(df['LoanAmount'])<20000:
				messages.success(request,'Status: {}'.format(answer))
			else:
				messages.success(request,'Invalid: Your Loan Request Exceeds $20,000 Limit')
	
	form=ApprovalForm()
				
	return render(request, 'forms/form.html', {'form':form})