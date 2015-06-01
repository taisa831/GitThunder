myForm = new Validate();
myForm.addRules({id:'pwd',option:'required',error:'パスワード：必須です'});
myForm.addRules({id:'user',option:'email',error:'メール：アドレスが不正です'});
